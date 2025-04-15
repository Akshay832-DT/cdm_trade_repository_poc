"""
Test FIX message parsing using generated Pydantic models.
"""
import unittest
import asyncio
from datetime import datetime, date
from src.parsers.controller import ParserController
from src.models.fix.generated.messages.bidresponse import BidResponseMessage
from src.models.fix.generated.components.bidcomprspgrp import NoBidComponentsGroup

class TestFIXParser(unittest.TestCase):
    """Test FIX message parsing functionality."""
    
    def setUp(self):
        self.parser_controller = ParserController()
    
    def test_bid_response_parsing(self):
        """Test parsing a BidResponse message."""
        # Raw FIX message string (pipe symbol as separator for readability, will be replaced with SOH)
        raw_fix_message = (
            "8=FIX.4.4|9=489|35=l|34=1|49=SENDER|56=TARGET|52=20240412-14:30:00|"
            # BidResponse fields
            "390=BID123|391=CLIENT123|398=0|"
            # Instrument fields
            "55=AAPL|48=US0378331005|22=8|167=CS|200=202412|541=20241231|15=USD|"
            # Parties fields
            "453=1|448=PARTY123|447=D|452=1|"
            # BidComponents fields
            "420=1|66=LIST123|421=US|54=1|44=100.50|423=1|406=101.25|430=1|63=0|"
            "64=20241231|336=TSE1|625=MORNING|58=Sample bid component|"
            # CommissionData fields within BidComponents
            "12=1.25|13=1|479=USD|10=123"
        ).replace("|", "\x01")  # Replace pipe with SOH character
        
        # Parse the message asynchronously
        message = asyncio.run(self.parser_controller.parse_message(raw_fix_message, 'FIX'))
        
        # Verify message is correctly parsed as BidResponseMessage
        self.assertIsInstance(message, BidResponseMessage)
        
        # Verify header fields
        self.assertEqual(message.BeginString, "FIX.4.4")
        self.assertEqual(message.MsgType, "l")
        self.assertEqual(message.SenderCompID, "SENDER")
        self.assertEqual(message.TargetCompID, "TARGET")
        self.assertEqual(message.MsgSeqNum, 1)
        
        # Verify BidResponse fields
        self.assertEqual(message.BidID, "BID123")
        self.assertEqual(message.ClientBidID, "CLIENT123")
        
        # Verify Instrument fields
        self.assertEqual(message.Instrument.Symbol, "AAPL")
        self.assertEqual(message.Instrument.SecurityID, "US0378331005")
        self.assertEqual(message.Instrument.SecurityIDSource, "8")
        self.assertEqual(message.Instrument.SecurityType, "CS")
        self.assertEqual(message.Instrument.Currency, "USD")
        
        # Verify Parties fields
        self.assertEqual(message.Parties.NoParty, 1)
        party = message.Parties.NoParty_items[0]
        self.assertEqual(party.PartyID, "PARTY123")
        self.assertEqual(party.PartyIDSource, "D")
        self.assertEqual(party.PartyRole, 1)
        
        # Verify BidComponents fields
        self.assertEqual(message.BidCompRspGrp.NoBidComponents, 1)
        bid_component = message.BidCompRspGrp.NoBidComponents_items[0]
        self.assertEqual(bid_component.ListID, "LIST123")
        self.assertEqual(bid_component.Country, "US")
        self.assertEqual(bid_component.Side, "1")
        self.assertEqual(bid_component.Price, 100.50)
        self.assertEqual(bid_component.PriceType, 1)
        self.assertEqual(bid_component.FairValue, 101.25)
        self.assertEqual(bid_component.NetGrossInd, 1)
        self.assertEqual(bid_component.SettlType, "0")
        self.assertEqual(bid_component.SettlDate, date(2024, 12, 31))
        self.assertEqual(bid_component.TradingSessionID, "TSE1")
        self.assertEqual(bid_component.TradingSessionSubID, "MORNING")
        self.assertEqual(bid_component.Text, "Sample bid component")
        
        # Verify CommissionData fields
        self.assertEqual(bid_component.CommissionData.Commission, 1.25)
        self.assertEqual(bid_component.CommissionData.CommType, "1")
        self.assertEqual(bid_component.CommissionData.CommCurrency, "USD")

if __name__ == '__main__':
    unittest.main() 