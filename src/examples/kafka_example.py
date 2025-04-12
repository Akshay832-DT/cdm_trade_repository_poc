import asyncio
import logging
from ..processors.kafka_processor import KafkaProcessor
from ..parsers.controller import ParserController
from ..models.base import TradeModel

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Define message processors
async def process_fix_message(message: TradeModel):
    """Process a parsed FIX message."""
    logger.info(f"Processing FIX message: {message.model_dump()}")
    # Add application-specific processing logic here

async def process_fpml_message(message: TradeModel):
    """Process a parsed FpML message."""
    logger.info(f"Processing FpML message: {message.model_dump()}")
    # Add application-specific processing logic here

async def process_cdm_message(message: TradeModel):
    """Process a parsed CDM message."""
    logger.info(f"Processing CDM message: {message.model_dump()}")
    # Add application-specific processing logic here

async def main():
    # Initialize parser controller
    parser_controller = ParserController()
    
    # Configure Kafka processor
    kafka_processor = KafkaProcessor(
        bootstrap_servers="localhost:9092",
        topics=["fix_messages", "fpml_messages", "cdm_messages"],
        group_id="trade_processor",
        parser_controller=parser_controller,
        max_queue_size=1000
    )
    
    # Register message processors
    kafka_processor.register_processor("FIX", process_fix_message)
    kafka_processor.register_processor("FPML", process_fpml_message)
    kafka_processor.register_processor("CDM", process_cdm_message)
    
    # Start the Kafka processor
    await kafka_processor.start()
    
    try:
        # Keep the application running
        while True:
            # Monitor queue sizes
            queue_sizes = await kafka_processor.get_queue_sizes()
            for topic, size in queue_sizes.items():
                if size > 0:
                    logger.info(f"Queue size for {topic}: {size}")
            
            await asyncio.sleep(10)  # Check every 10 seconds
    except KeyboardInterrupt:
        logger.info("Shutting down...")
    finally:
        # Stop the Kafka processor
        await kafka_processor.stop()

if __name__ == "__main__":
    asyncio.run(main()) 