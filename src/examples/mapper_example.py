"""
Example script demonstrating usage of FIX and FPML to CDM mappers
"""
import asyncio
import logging
import json
import os
from pathlib import Path
from datetime import datetime, date

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import mappers
from src.mappers.controller import MapperController
from src.mappers.utils.mapping_tracker import MappingTracker

# Import models
from src.models.fix.generated.messages.executionreport import ExecutionReport
from src.models.fpml.generated.trade.trade import FpMLTrade, TradeHeader, PartyTradeIdentifier, PartyReference, Product
from src.models.fpml.generated.trade.trade import InterestRateProduct, SwapStream, PayerReceiver, NotionalAmount

async def create_sample_fix_execution_report():
    """
    Create a sample FIX execution report for testing
    
    Returns:
        ExecutionReport: Sample execution report
    """
    # Create a sample ExecutionReport object
    exec_report = ExecutionReport()
    
    # Set fields
    exec_report.ClOrdID = "CLORD-123456"
    exec_report.OrderID = "ORDER-654321"
    exec_report.ExecID = "EXEC-789012"
    exec_report.ExecType = "2"  # FILL
    exec_report.OrdStatus = "2"  # FILLED
    exec_report.Symbol = "AAPL"
    exec_report.Side = "1"  # BUY
    exec_report.OrderQty = 100
    exec_report.OrdType = "2"  # LIMIT
    exec_report.Price = 150.25
    exec_report.Currency = "USD"
    exec_report.TimeInForce = "0"  # DAY
    exec_report.LastQty = 100
    exec_report.LastPx = 150.25
    exec_report.AvgPx = 150.25
    exec_report.TransactTime = datetime.now().strftime("%Y%m%d-%H:%M:%S")
    exec_report.Text = "Sample execution report"
    
    return exec_report

def create_sample_fpml_trade():
    """
    Create a sample FpML trade for testing
    
    Returns:
        FpMLTrade: Sample FpML trade
    """
    # Create trade header
    trade_header = TradeHeader(
        partyTradeIdentifier=[
            PartyTradeIdentifier(
                partyReference=PartyReference(href="party1"),
                tradeId="TRADE-123456"
            ),
            PartyTradeIdentifier(
                partyReference=PartyReference(href="party2"),
                tradeId="TRADE-654321"
            )
        ],
        tradeDate=date.today()
    )
    
    # Create interest rate swap product
    swap_stream = SwapStream(
        payerReceiver=PayerReceiver(
            payerPartyReference=PartyReference(href="party1"),
            receiverPartyReference=PartyReference(href="party2")
        ),
        notionalAmount=NotionalAmount(
            amount=1000000.0,
            currency="USD"
        ),
        paymentFrequency="3M"
    )
    
    interest_rate_product = InterestRateProduct(
        swapStream=[swap_stream]
    )
    
    # Create product
    product = Product(
        interestRate=interest_rate_product
    )
    
    # Create FpML trade
    fpml_trade = FpMLTrade(
        tradeHeader=trade_header,
        product=product
    )
    
    return fpml_trade

async def main():
    """
    Main function demonstrating mapper usage
    """
    # Create mapper controller
    controller = MapperController()
    
    # Create mapping tracker
    tracker = MappingTracker()
    
    # Create output directory for reports
    output_dir = Path(__file__).parent / "mapping_reports"
    os.makedirs(output_dir, exist_ok=True)
    
    logger.info("Creating sample FIX execution report...")
    fix_message = await create_sample_fix_execution_report()
    
    logger.info("Mapping FIX execution report to CDM...")
    cdm_from_fix = controller.map_fix_to_cdm(fix_message)
    
    if cdm_from_fix:
        logger.info("Successfully mapped FIX execution report to CDM")
        fix_mapper = controller.get_fix_mapper("ExecutionReport")
        if fix_mapper:
            fix_stats = fix_mapper.get_mapping_stats()
            tracker.add_mapping_stats("FIX_ExecutionReport", fix_stats)
            logger.info(f"FIX mapping stats: {json.dumps(fix_stats, indent=2)}")
    else:
        logger.error("Failed to map FIX execution report to CDM")
    
    logger.info("Creating sample FpML trade...")
    fpml_trade = create_sample_fpml_trade()
    
    logger.info("Mapping FpML trade to CDM...")
    cdm_from_fpml = controller.map_fpml_to_cdm(fpml_trade)
    
    if cdm_from_fpml:
        logger.info("Successfully mapped FpML trade to CDM")
        fpml_mapper = controller.get_fpml_mapper("FpMLTrade")
        if fpml_mapper:
            fpml_stats = fpml_mapper.get_mapping_stats()
            tracker.add_mapping_stats("FPML_Trade", fpml_stats)
            logger.info(f"FPML mapping stats: {json.dumps(fpml_stats, indent=2)}")
    else:
        logger.error("Failed to map FpML trade to CDM")
    
    # Generate mapping report
    logger.info("Generating mapping report...")
    tracker.generate_report(output_dir)
    logger.info(f"Mapping report generated in {output_dir}")
    
    # Print overall statistics
    overall_stats = tracker.get_overall_stats()
    logger.info(f"Overall mapping stats: {json.dumps(overall_stats, indent=2)}")
    
    logger.info("Done!")

if __name__ == "__main__":
    asyncio.run(main()) 