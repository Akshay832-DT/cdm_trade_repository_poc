#!/usr/bin/env python3
import asyncio
import logging
from ..parsers.controller import ParserController

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Example messages
FIX_MESSAGE = """8=FIX.4.4|9=123|35=D|49=SENDER|56=TARGET|34=1|52=20220101-12:00:00|11=OrderID|21=1|55=AAPL|54=1|60=20220101-12:00:00|38=100|40=2|44=150.00|10=000|"""

FPML_MESSAGE = """
<FpML xmlns="http://www.fpml.org/FpML-5/confirmation">
  <trade>
    <tradeHeader>
      <partyTradeIdentifier>
        <partyReference href="Party1"/>
        <tradeId>Trade123</tradeId>
      </partyTradeIdentifier>
      <tradeDate>2022-01-01</tradeDate>
    </tradeHeader>
    <product>
      <interestRate>
        <swapStream>
          <payerPartyReference href="Party1"/>
          <receiverPartyReference href="Party2"/>
          <paymentFrequency>Quarterly</paymentFrequency>
          <notional>1000000</notional>
          <currency>USD</currency>
        </swapStream>
      </interestRate>
    </product>
  </trade>
</FpML>
"""

CDM_MESSAGE = """
{
  "trade": {
    "tradeHeader": {
      "tradeIdentifier": [
        {
          "tradeId": "Trade123",
          "source": "Party1"
        }
      ],
      "tradeDate": "2022-01-01T00:00:00Z"
    },
    "product": {
      "interestRate": {
        "swapStream": [
          {
            "payerPartyReference": "Party1",
            "receiverPartyReference": "Party2",
            "paymentFrequency": "Quarterly",
            "notional": 1000000.0,
            "currency": "USD",
            "fixedRate": 0.025
          }
        ]
      }
    }
  }
}
"""

async def parse_examples():
    # Initialize parser controller
    parser_controller = ParserController()
    
    # Log supported formats
    logger.info(f"Supported formats: {parser_controller.get_supported_formats()}")
    
    try:
        # Parse FIX message
        logger.info("Parsing FIX message...")
        fix_parsed = await parser_controller.parse_message(FIX_MESSAGE, "FIX")
        logger.info(f"FIX parsed result: {fix_parsed.to_json()}")
        
        # Parse FpML message
        logger.info("Parsing FpML message...")
        fpml_parsed = await parser_controller.parse_message(FPML_MESSAGE, "FPML")
        logger.info(f"FpML parsed result: {fpml_parsed.to_json()}")
        
        # Parse CDM message
        logger.info("Parsing CDM message...")
        cdm_parsed = await parser_controller.parse_message(CDM_MESSAGE, "CDM")
        logger.info(f"CDM parsed result: {cdm_parsed.to_json()}")
        
    except Exception as e:
        logger.error(f"Error parsing messages: {str(e)}")

if __name__ == "__main__":
    asyncio.run(parse_examples()) 