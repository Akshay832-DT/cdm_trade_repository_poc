"""
Test parsing an Interest Rate Swap FIX message and validate the created objects.
"""
import unittest
import asyncio
import sys
from datetime import datetime, date
import simplefix
from src.parsers.controller import ParserController
from src.models.fix.generated.messages.newordersingle import NewOrderSingle
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.orderqtydata import OrderQtyData
from src.parsers.fix.parser import FIXParser

class TestIRSMessageParsing(unittest.TestCase):
    """Test parsing Interest Rate Swap FIX message and object validation."""
    
    def setUp(self):
        self.parser_controller = ParserController()
        self.parser = FIXParser()
        
        # Standard FIX message for IRS
        self.raw_fix_message = (
            b"8=FIX.4.4\x01"
            b"9=123\x01"
            b"35=D\x01"
            b"49=SENDER\x01"
            b"56=TARGET\x01"
            b"34=1\x01"
            b"52=20240412-14:30:00\x01"
            b"11=ORDER123\x01"
            b"1=ACCOUNT123\x01"
            b"54=1\x01"
            b"40=2\x01"
            b"44=100.50\x01"
            b"59=0\x01"
            b"55=SWAP\x01"
            b"167=SWAP\x01"
            b"200=202404\x01"
            b"541=20240415\x01"
            b"947=USD\x01"
            b"460=4\x01"
            b"38=1000000\x01"
            b"152=1000000\x01"
            b"60=20240412-14:30:00\x01"
            b"48=SWAP123\x01"
            b"22=8\x01"
            b"207=NYSE\x01"
            b"107=Interest Rate Swap\x01"
            b"10=123\x01"
        )
    
    def test_simplefix_direct_parse(self):
        """Test direct parsing using simplefix to verify message structure."""
        parser = simplefix.FixParser()
        parser.append_buffer(self.raw_fix_message)
        msg = parser.get_message()
        
        self.assertIsNotNone(msg, "Message should be parsed successfully")
        self.assertEqual(msg.get(8).decode(), "FIX.4.4", "BeginString should match")
        self.assertEqual(msg.get(35).decode(), "D", "MsgType should be NewOrderSingle")
        self.assertEqual(msg.get(167).decode(), "SWAP", "SecurityType should be SWAP")
        self.assertEqual(msg.get(460).decode(), "4", "Product should be Interest Rate")
    
    def test_fix_parser_validation(self):
        """Test that the FIX parser correctly validates a raw FIX message."""
        async def run_test():
            parser = simplefix.FixParser()
            parser.append_buffer(self.raw_fix_message)
            fix_msg = parser.get_message()
            
            self.assertTrue(await self.parser.validate(self.raw_fix_message.decode()), "Message should be valid")
            
            parsed_data = self.parser._parse_fields(fix_msg)
            self.assertEqual(parsed_data['8'], 'FIX.4.4')
            self.assertEqual(parsed_data['35'], 'D')
            self.assertEqual(parsed_data['167'], 'SWAP')
            self.assertEqual(parsed_data['460'], '4')
        
        asyncio.run(run_test())
    
    def test_full_message_parse(self):
        """Test full message parsing through the ParserController."""
        async def run_test():
            # Parse the message first to get a FixMessage object
            parser = simplefix.FixParser()
            parser.append_buffer(self.raw_fix_message)
            fix_msg = parser.get_message()
            
            # Now parse through the controller
            message = await self.parser_controller.parse_message(fix_msg, 'FIX')
            
            # Verify message is correctly parsed as NewOrderSingle
            self.assertIsInstance(message, NewOrderSingle)
            
            # Verify header fields
            self.assertEqual(message.beginstring, "FIX.4.4")
            self.assertEqual(message.msgtype, "D")
            self.assertEqual(message.sendercompid, "SENDER")
            self.assertEqual(message.targetcompid, "TARGET")
            self.assertEqual(message.msgseqnum, 1)
            
            # Verify order fields
            self.assertEqual(message.clordid, "ORDER123")
            self.assertEqual(message.account, "ACCOUNT123")
            self.assertEqual(message.side, "1")
            self.assertEqual(message.ordtype, "2")
            self.assertEqual(message.price, 100.50)
            self.assertEqual(message.timeinforce, "0")
            
            # Verify OrderQtyData fields
            self.assertEqual(message.orderqtydata.orderQty, 1000000)
            self.assertEqual(message.orderqtydata.cashOrderQty, 1000000)
            
            # Verify instrument fields
            self.assertEqual(message.instrument.symbol, "SWAP")
            self.assertEqual(message.instrument.securityType, "SWAP")
            self.assertEqual(message.instrument.maturityMonthYear, "202404")
            self.assertEqual(message.instrument.maturityDate, date(2024, 4, 15))
            self.assertEqual(message.instrument.strikeCurrency, "USD")
            self.assertEqual(message.instrument.product, 4)
        
        asyncio.run(run_test())

if __name__ == '__main__':
    unittest.main() 