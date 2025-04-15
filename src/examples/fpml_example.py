#!/usr/bin/env python3
"""
FpML Example Script

This script demonstrates the complete process of:
1. Downloading FpML schema files
2. Generating Pydantic models
3. Parsing FpML messages using those models

Usage:
    python -m src.examples.fpml_example
"""
import asyncio
import logging
import sys
from pathlib import Path
from typing import Dict, Any
import argparse

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import necessary modules
from src.generators.fpml_schema_downloader import download_fpml_schemas, validate_schema_files
from src.generators.fpml_model_generator import main as generate_models
from src.parsers.controller import ParserController

# Example FpML messages
IRS_FPML_MESSAGE = """
<FpML xmlns="http://www.fpml.org/FpML-5/confirmation">
  <trade>
    <tradeHeader>
      <partyTradeIdentifier>
        <partyReference href="Party1"/>
        <tradeId>TRADE123</tradeId>
      </partyTradeIdentifier>
      <partyTradeIdentifier>
        <partyReference href="Party2"/>
        <tradeId>TRADE456</tradeId>
      </partyTradeIdentifier>
      <tradeDate>2024-04-12</tradeDate>
    </tradeHeader>
    <product>
      <interestRate>
        <swapStream>
          <payerReceiver>
            <payerPartyReference href="Party1"/>
            <receiverPartyReference href="Party2"/>
          </payerReceiver>
          <paymentFrequency>Quarterly</paymentFrequency>
          <notionalAmount>
            <amount>10000000</amount>
            <currency>USD</currency>
          </notionalAmount>
        </swapStream>
        <swapStream>
          <payerReceiver>
            <payerPartyReference href="Party2"/>
            <receiverPartyReference href="Party1"/>
          </payerReceiver>
          <paymentFrequency>Quarterly</paymentFrequency>
          <notionalAmount>
            <amount>10000000</amount>
            <currency>USD</currency>
          </notionalAmount>
        </swapStream>
      </interestRate>
    </product>
  </trade>
</FpML>
"""

CDS_FPML_MESSAGE = """
<FpML xmlns="http://www.fpml.org/FpML-5/confirmation">
  <trade>
    <tradeHeader>
      <partyTradeIdentifier>
        <partyReference href="Party1"/>
        <tradeId>CDS12345</tradeId>
      </partyTradeIdentifier>
      <partyTradeIdentifier>
        <partyReference href="Party2"/>
        <tradeId>CDS67890</tradeId>
      </partyTradeIdentifier>
      <tradeDate>2024-04-12</tradeDate>
    </tradeHeader>
    <product>
      <credit>
        <protectionTerms>
          <referenceEntity>ACME Corporation</referenceEntity>
          <creditEvent>Bankruptcy</creditEvent>
          <settlementType>Physical</settlementType>
        </protectionTerms>
        <referenceInformation>
          <referenceEntity>ACME Corporation</referenceEntity>
          <referenceObligation>ACME 5.75% 2028</referenceObligation>
        </referenceInformation>
      </credit>
    </product>
  </trade>
</FpML>
"""

async def download_and_generate(fpml_version: str, force: bool = False):
    """Download schemas and generate models."""
    logger.info(f"Step 1: Downloading FpML {fpml_version} schemas...")
    download_fpml_schemas(fpml_version, force)
    
    if not validate_schema_files(fpml_version):
        logger.error("Failed to download and validate schemas")
        sys.exit(1)
    
    logger.info(f"Step 2: Generating Pydantic models from FpML {fpml_version} schemas...")
    # Create a simple argparse Namespace with the required arguments
    class Args:
        version = fpml_version
        force = force
    
    # Call the model generator
    generate_models(Args())
    
    logger.info("Model generation complete!")

async def parse_messages():
    """Parse example FpML messages."""
    logger.info("Step 3: Parsing FpML messages...")
    
    # Create parser controller
    controller = ParserController()
    
    # Parse IRS message
    logger.info("Parsing Interest Rate Swap message...")
    irs_trade = await controller.parse_message(IRS_FPML_MESSAGE, 'FPML')
    logger.info(f"IRS Trade ID: {irs_trade.tradeHeader.partyTradeIdentifier[0].tradeId}")
    logger.info(f"IRS Trade Date: {irs_trade.tradeHeader.tradeDate}")
    logger.info(f"IRS Notional: {irs_trade.product.interestRate.swapStream[0].notionalAmount.amount} {irs_trade.product.interestRate.swapStream[0].notionalAmount.currency}")
    
    # Parse CDS message
    logger.info("Parsing Credit Default Swap message...")
    cds_trade = await controller.parse_message(CDS_FPML_MESSAGE, 'FPML')
    logger.info(f"CDS Trade ID: {cds_trade.tradeHeader.partyTradeIdentifier[0].tradeId}")
    logger.info(f"CDS Trade Date: {cds_trade.tradeHeader.tradeDate}")
    logger.info(f"CDS Reference Entity: {cds_trade.product.credit.referenceInformation.referenceEntity}")
    
    return True

async def run_example(fpml_version: str, force: bool, skip_download: bool):
    """Run the full example."""
    try:
        if not skip_download:
            # Step 1 & 2: Download schemas and generate models
            await download_and_generate(fpml_version, force)
        
        # Step 3: Parse messages
        success = await parse_messages()
        
        if success:
            logger.info("FpML example completed successfully!")
        else:
            logger.error("FpML example failed")
            sys.exit(1)
    
    except Exception as e:
        logger.error(f"Error running FpML example: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="FpML Example Script")
    parser.add_argument(
        "--version", 
        default="5-10",
        help="FpML version to use (default: 5-10)"
    )
    parser.add_argument(
        "--force", 
        action="store_true", 
        help="Force download and regeneration of schemas and models"
    )
    parser.add_argument(
        "--skip-download", 
        action="store_true", 
        help="Skip downloading schemas and generating models, only run parsing example"
    )
    
    args = parser.parse_args()
    
    # Run the example asynchronously
    asyncio.run(run_example(args.version, args.force, args.skip_download))

if __name__ == "__main__":
    main() 