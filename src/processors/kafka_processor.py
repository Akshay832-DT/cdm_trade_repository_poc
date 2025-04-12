import json
import logging
import asyncio
from typing import Dict, Optional, List, Callable
from aiokafka import AIOKafkaConsumer
from aiokafka.errors import KafkaError
from ..parsers.controller import ParserController
from ..models.base import TradeModel

class KafkaProcessor:
    def __init__(
        self, 
        bootstrap_servers: str, 
        topics: List[str],
        group_id: str,
        parser_controller: Optional[ParserController] = None,
        message_processors: Optional[Dict[str, Callable]] = None,
        max_queue_size: int = 1000
    ):
        self.bootstrap_servers = bootstrap_servers
        self.topics = topics
        self.group_id = group_id
        self.parser_controller = parser_controller or ParserController()
        self.message_processors = message_processors or {}
        self.logger = logging.getLogger(__name__)
        self.running = False
        self.consumer = None
        self.processing_tasks = set()
        self.queue_sizes = {topic: 0 for topic in topics}
        self.max_queue_size = max_queue_size
    
    async def start(self):
        """Start the Kafka consumer."""
        if self.running:
            return
            
        self.logger.info(f"Starting Kafka consumer for topics {self.topics}")
        self.consumer = AIOKafkaConsumer(
            *self.topics,
            bootstrap_servers=self.bootstrap_servers,
            group_id=self.group_id,
            enable_auto_commit=False,
            auto_offset_reset="earliest"
        )
        
        await self.consumer.start()
        self.running = True
        
        # Start consuming messages
        asyncio.create_task(self._consume_messages())
    
    async def stop(self):
        """Stop the Kafka consumer."""
        if not self.running:
            return
            
        self.logger.info("Stopping Kafka consumer")
        self.running = False
        
        # Wait for all processing tasks to complete
        if self.processing_tasks:
            self.logger.info(f"Waiting for {len(self.processing_tasks)} processing tasks to complete")
            await asyncio.gather(*self.processing_tasks, return_exceptions=True)
        
        # Stop the consumer
        if self.consumer:
            await self.consumer.stop()
            
        self.logger.info("Kafka consumer stopped")
    
    async def _consume_messages(self):
        """Consume messages from Kafka topics."""
        try:
            async for message in self.consumer:
                # Track queue size for monitoring
                topic = message.topic
                self.queue_sizes[topic] = self.queue_sizes.get(topic, 0) + 1
                
                # Check if queue size exceeds threshold
                if self.queue_sizes[topic] > self.max_queue_size:
                    self.logger.warning(f"Queue size for topic {topic} exceeds threshold: {self.queue_sizes[topic]}")
                
                # Process message
                task = asyncio.create_task(self._process_message(message))
                self.processing_tasks.add(task)
                task.add_done_callback(self.processing_tasks.remove)
        except Exception as e:
            self.logger.error(f"Error consuming messages: {str(e)}")
            if self.running:
                self.logger.info("Restarting consumer...")
                await asyncio.sleep(1)  # Wait before restarting
                asyncio.create_task(self._consume_messages())
    
    async def _process_message(self, message):
        """Process a Kafka message."""
        try:
            topic = message.topic
            key = message.key.decode() if message.key else None
            value = message.value.decode()
            
            self.logger.debug(f"Processing message from topic {topic}: {key}")
            
            # Determine message format (FIX, FpML, CDM)
            message_format = self._detect_message_format(value)
            if not message_format:
                self.logger.warning(f"Unknown message format: {value[:100]}...")
                await self.consumer.commit({message.partition: message.offset + 1})
                return
            
            # Parse message
            try:
                parsed_message = await self.parser_controller.parse_message(value, message_format)
                
                # Process parsed message with registered processor
                if message_format in self.message_processors:
                    await self.message_processors[message_format](parsed_message)
                else:
                    self.logger.warning(f"No processor registered for format: {message_format}")
                
                self.logger.debug(f"Successfully processed {message_format} message")
            except Exception as e:
                self.logger.error(f"Error parsing message: {str(e)}")
            
            # Update queue size after processing
            self.queue_sizes[topic] = max(0, self.queue_sizes.get(topic, 0) - 1)
            
            # Commit offset
            await self.consumer.commit({message.partition: message.offset + 1})
        except Exception as e:
            self.logger.error(f"Error processing message: {str(e)}")
    
    def _detect_message_format(self, message: str) -> Optional[str]:
        """
        Detect the format of a message.
        Returns 'FIX', 'FPML', 'CDM', or None if unknown.
        """
        # Try to detect FIX format (starts with 8=FIX)
        if message.startswith('8=FIX'):
            return 'FIX'
        
        # Try to detect FpML (XML format with fpml namespace)
        if message.startswith('<') and ('fpml' in message.lower() or 'xmlns' in message.lower()):
            return 'FPML'
        
        # Try to detect CDM (JSON format)
        try:
            data = json.loads(message)
            if isinstance(data, dict) and any(k in data for k in ['trade', 'event', 'lifecycle']):
                return 'CDM'
        except json.JSONDecodeError:
            pass
        
        return None
    
    def register_processor(self, message_format: str, processor: Callable):
        """Register a processor function for a specific message format."""
        self.message_processors[message_format] = processor
        self.logger.info(f"Registered processor for {message_format} messages")
    
    async def get_queue_sizes(self) -> Dict[str, int]:
        """Get the current queue sizes for all topics."""
        return self.queue_sizes 