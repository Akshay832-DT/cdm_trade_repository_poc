"""
Test parsing an Interest Rate Swap FIX message and validate the created objects.
"""
import unittest
import asyncio
import sys
from datetime import datetime, date
import simplefix
from src.parsers.controller import ParserController
from src.models.fix.generated.messages.newordersingle import NewOrderSingleMessage
from src.models.fix.generated.components.instrument import InstrumentComponent
from src.models.fix.generated.components.orderqtydata import OrderQtyDataComponent
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
    
    async def test_fix_parser_validation(self):
        """Test that the FIX parser correctly validates a raw FIX message."""
        self.assertTrue(await self.parser.validate(self.raw_fix_message), "Message should be valid")
        parsed_data = await self.parser.parse(self.raw_fix_message)
        
        # Verify common fields
        self.assertEqual(parsed_data.BeginString, 'FIX.4.4')
        self.assertEqual(parsed_data.MsgType, 'D')
        self.assertEqual(parsed_data.SenderCompID, 'SENDER')
        self.assertEqual(parsed_data.TargetCompID, 'TARGET')
        
        # Verify IRS specific fields
        self.assertEqual(parsed_data.Instrument.SecurityType, 'SWAP')
        self.assertEqual(parsed_data.Instrument.MaturityMonthYear, '202404')
        self.assertEqual(parsed_data.Instrument.MaturityDate.strftime('%Y%m%d'), '20240415')
        
        # Verify order fields
        self.assertEqual(parsed_data.ClOrdID, 'ORDER123')
        self.assertEqual(parsed_data.Account, 'ACCOUNT123')
        self.assertEqual(parsed_data.Side, '1')
        self.assertEqual(parsed_data.OrdType, '2')
        self.assertEqual(parsed_data.Price, 100.50)
        self.assertEqual(parsed_data.Instrument.StrikeCurrency, 'USD')
    
    def test_full_message_parse(self):
        """Test full message parsing through the ParserController."""
        async def run_test():
            # Parse the message first to get a FixMessage object
            parser = simplefix.FixParser()
            parser.append_buffer(self.raw_fix_message)
            fix_msg = parser.get_message()
            
            # Now parse through the controller
            message = await self.parser_controller.parse_message(fix_msg, 'FIX')
            
            # Verify message is correctly parsed as NewOrderSingleMessage
            self.assertIsInstance(message, NewOrderSingleMessage)
            
            # Verify header fields
            self.assertEqual(message.BeginString, "FIX.4.4")
            self.assertEqual(message.MsgType, "D")
            self.assertEqual(message.SenderCompID, "SENDER")
            self.assertEqual(message.TargetCompID, "TARGET")
            self.assertEqual(message.MsgSeqNum, 1)
            
            # Verify order fields
            self.assertEqual(message.ClOrdID, "ORDER123")
            self.assertEqual(message.Account, "ACCOUNT123")
            self.assertEqual(message.Side, "1")
            self.assertEqual(message.OrdType, "2")
            self.assertEqual(message.Price, 100.50)
            self.assertEqual(message.TimeInForce, "0")
            
            # Verify OrderQtyData fields
            self.assertEqual(message.OrderQtyData.OrderQty, 1000000)
            self.assertEqual(message.OrderQtyData.CashOrderQty, 1000000)
            
            # Verify instrument fields
            self.assertEqual(message.Instrument.Symbol, "SWAP")
            self.assertEqual(message.Instrument.SecurityType, "SWAP")
            self.assertEqual(message.Instrument.MaturityMonthYear, "202404")
            self.assertEqual(message.Instrument.MaturityDate, date(2024, 4, 15))
            self.assertEqual(message.Instrument.StrikeCurrency, "USD")
            self.assertEqual(message.Instrument.Product, 4)
        
        asyncio.run(run_test())

if __name__ == '__main__':
    unittest.main() 