"""
Test parsing a BID response FIX message and validate the created objects.
"""
import unittest
import asyncio
import sys
from datetime import datetime, date
import simplefix
from src.parsers.controller import ParserController
from src.models.fix.generated.messages.bidresponse import BidResponseMessage
from src.models.fix.generated.components.bidcomprspgrp import BidCompRspGrpComponent, NoBidComponentsGroup
from src.models.fix.generated.components.commissiondata import CommissionDataComponent
from src.parsers.fix.parser import FIXParser

class TestBidResponseParsing(unittest.TestCase):
    """Test parsing BID response FIX message and object validation."""
    
    def setUp(self):
        self.parser_controller = ParserController()
        self.parser = FIXParser()
        
        # Standard FIX message used across tests
        self.raw_fix_message = (
            "8=FIX.4.4\x01"       # BeginString
            "9=220\x01"           # BodyLength
            "35=l\x01"            # MsgType (BidResponse)
            "34=1\x01"            # MsgSeqNum
            "49=SENDER\x01"       # SenderCompID
            "56=TARGET\x01"       # TargetCompID
            "52=20240412-14:30:00\x01"  # SendingTime
            
            # BidResponse fields
            "390=BID123\x01"      # BidID
            "391=CLIENT123\x01"   # ClientBidID
            "398=0\x01"           # NoClientBidIDs
            
            # BidComponents fields
            "420=1\x01"           # NoBidComponents
            "66=LIST123\x01"      # ListID
            "421=US\x01"          # Country
            "54=1\x01"            # Side
            "44=100.50\x01"       # Price
            "423=1\x01"           # PriceType
            "406=101.25\x01"      # FairValue
            "430=1\x01"           # NetGrossInd
            "63=0\x01"            # SettlType
            "64=20241231\x01"     # SettlDate
            "336=TSE1\x01"        # TradingSessionID
            "625=MORNING\x01"     # TradingSessionSubID
            "58=Sample bid component\x01"  # Text
            
            # CommissionData fields
            "12=1.25\x01"         # Commission
            "13=1\x01"            # CommType
            "479=USD\x01"         # CommCurrency
            
            "10=248\x01"          # CheckSum
        )
    
    def test_simplefix_direct_parse(self):
        """Test direct parsing using simplefix to verify message structure."""
        parser = simplefix.FixParser()
        parser.append_buffer(self.raw_fix_message.encode())
        msg = parser.get_message()
        
        self.assertIsNotNone(msg, "Message should be parsed successfully")
        self.assertEqual(msg.get(8).decode(), "FIX.4.4", "BeginString should match")
        self.assertEqual(msg.get(35).decode(), "l", "MsgType should be BidResponse")
        self.assertEqual(msg.get(12).decode(), "1.25", "Commission value should match")
        self.assertEqual(msg.get(13).decode(), "1", "CommType should match")
        self.assertEqual(msg.get(479).decode(), "USD", "CommCurrency should match")
    
    def test_fix_parser_validation(self):
        """Test FIX parser validation of the message."""
        async def run_test():
            parser = simplefix.FixParser()
            parser.append_buffer(self.raw_fix_message.encode())
            fix_msg = parser.get_message()
            
            self.assertTrue(await self.parser.validate(self.raw_fix_message.encode()), "Message should be valid")
            
            parsed_data = self.parser._parse_fields(fix_msg)
            self.assertEqual(parsed_data[8], 'FIX.4.4')
            self.assertEqual(parsed_data[35], 'l')
            self.assertEqual(parsed_data[49], 'SENDER')
            self.assertEqual(parsed_data[56], 'TARGET')
            self.assertEqual(str(parsed_data[34]), '1')  # Convert to string for comparison
        
        asyncio.run(run_test())
    
    def test_full_message_parse(self):
        """Test full message parsing through the ParserController."""
        async def run_test():
            # Parse the message first to get a FixMessage object
            parser = simplefix.FixParser()
            parser.append_buffer(self.raw_fix_message.encode())
            fix_msg = parser.get_message()
            
            # Now parse through the controller
            message = await self.parser_controller.parse_message(fix_msg, 'FIX')
            
            # Verify message is correctly parsed as BidResponseMessage
            self.assertIsInstance(message, BidResponseMessage)
            
            # Verify header fields
            self.assertEqual(message.BeginString, "FIX.4.4")
            self.assertEqual(message.MsgType, "l")
            self.assertEqual(message.SenderCompID, "SENDER")
            self.assertEqual(message.TargetCompID, "TARGET")
            self.assertEqual(message.MsgSeqNum, 1)
            
            # Verify BidResponse specific fields
            self.assertEqual(message.BidID, "BID123")
            self.assertEqual(message.ClientBidID, "CLIENT123")
            
            # Verify BidCompRspGrp fields
            self.assertEqual(message.BidCompRspGrp.NoBidComponents, 1)
            
            # Access the bid component group item
            bid_component = message.BidCompRspGrp.NoBidComponents_items[0]
            
            # Verify NoBidComponents fields
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
            self.assertEqual(bid_component.CommissionData.CommType, '1')
            self.assertEqual(bid_component.CommissionData.CommCurrency, "USD")
        
        asyncio.run(run_test())

if __name__ == '__main__':
    unittest.main() 