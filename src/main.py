#!/usr/bin/env python3
import asyncio
import logging
import os
import signal
from processors.kafka_processor import KafkaProcessor
from parsers.controller import ParserController
from models.base import TradeModel

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Define message processors
async def process_message(message: TradeModel):
    """Generic message processor that logs the message."""
    message_type = message.__class__.__name__
    logger.info(f"Processed {message_type}")
    # In a real application, you would store the message in the database,
    # perform additional processing, etc.

# Global reference to the Kafka processor for graceful shutdown
kafka_processor = None

async def main():
    global kafka_processor
    
    # Get configuration from environment variables
    bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
    topics = os.getenv("KAFKA_TOPICS", "fix_messages,fpml_messages,cdm_messages").split(",")
    group_id = os.getenv("KAFKA_GROUP_ID", "trade_processor")
    max_queue_size = int(os.getenv("MAX_QUEUE_SIZE", "1000"))
    
    logger.info(f"Starting trade repository with the following configuration:")
    logger.info(f"Kafka bootstrap servers: {bootstrap_servers}")
    logger.info(f"Kafka topics: {topics}")
    logger.info(f"Kafka consumer group ID: {group_id}")
    logger.info(f"Maximum queue size: {max_queue_size}")
    
    # Initialize parser controller
    parser_controller = ParserController()
    
    # Configure Kafka processor
    kafka_processor = KafkaProcessor(
        bootstrap_servers=bootstrap_servers,
        topics=topics,
        group_id=group_id,
        parser_controller=parser_controller,
        max_queue_size=max_queue_size
    )
    
    # Register message processors
    for format_type in parser_controller.get_supported_formats():
        kafka_processor.register_processor(format_type, process_message)
    
    # Start the Kafka processor
    await kafka_processor.start()
    
    # Setup signal handlers for graceful shutdown
    loop = asyncio.get_event_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, lambda: asyncio.create_task(shutdown()))
    
    try:
        # Keep the application running and monitor queue sizes
        while True:
            # Monitor queue sizes
            queue_sizes = await kafka_processor.get_queue_sizes()
            for topic, size in queue_sizes.items():
                if size > 0:
                    logger.info(f"Queue size for {topic}: {size}")
                if size > max_queue_size:
                    logger.warning(f"Queue size for {topic} exceeds threshold: {size}")
            
            await asyncio.sleep(10)  # Check every 10 seconds
    except Exception as e:
        logger.error(f"Error in main loop: {str(e)}")
        await shutdown()

async def shutdown():
    """Gracefully shut down the application."""
    logger.info("Shutting down...")
    if kafka_processor:
        await kafka_processor.stop()
    
    tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
    if tasks:
        logger.info(f"Waiting for {len(tasks)} tasks to complete...")
        await asyncio.gather(*tasks, return_exceptions=True)
    
    asyncio.get_event_loop().stop()

if __name__ == "__main__":
    asyncio.run(main()) 