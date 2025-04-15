"""
Test parsing a Single Name CDS FIX message and validate the created objects.
"""
import unittest
import pytest
import simplefix
from datetime import datetime, date
from src.parsers.controller import ParserController
from src.parsers.fix.parser import FIXParser
from src.models.fix.generated.messages.newordersingle import NewOrderSingleMessage

class TestSingleNameCDSMessage(unittest.TestCase):
    """Test cases for Single Name CDS message parsing."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.parser = FIXParser()
        self.controller = ParserController()
        
        # Example Single Name CDS NewOrderSingle message
        self.fix_message = (
            b"8=FIX.4.4\x01"
            b"9=123\x01"
            b"35=D\x01"
            b"49=SENDER\x01"
            b"56=TARGET\x01"
            b"34=1\x01"
            b"52=20240412-14:30:00\x01"
            b"11=CDS12345\x01"
            b"1=ACCOUNT123\x01"
            b"21=1\x01"
            b"55=CDS\x01"
            b"48=CDS12345\x01"
            b"22=8\x01"
            b"167=CDS\x01"
            b"200=202412\x01"
            b"541=20241215\x01"
            b"207=XCDS\x01"
            b"460=4\x01"
            b"38=1000000\x01"
            b"40=2\x01"
            b"44=100.25\x01"
            b"54=1\x01"
            b"59=0\x01"
            b"60=20240412-14:30:00\x01"
            b"77=O\x01"
            b"10=123\x01"
        )
        
    def test_fix_message_parsing(self):
        """Test direct FIX message parsing."""
        parser = simplefix.FixParser()
        parser.append_buffer(self.fix_message)
        message = parser.get_message()
        
        # Test basic fields
        self.assertEqual(message.get(8).decode(), "FIX.4.4")
        self.assertEqual(message.get(35).decode(), "D")
        self.assertEqual(message.get(49).decode(), "SENDER")
        self.assertEqual(message.get(56).decode(), "TARGET")
        
        # Test CDS-specific fields
        self.assertEqual(message.get(55).decode(), "CDS")
        self.assertEqual(message.get(48).decode(), "CDS12345")
        self.assertEqual(message.get(167).decode(), "CDS")
        self.assertEqual(message.get(460).decode(), "4")  # Product = CDS
        
    @pytest.mark.asyncio
    async def test_fix_parser_validation(self):
        """Test FIX parser validation."""
        # Test valid message
        self.assertTrue(await self.parser.validate(self.fix_message))
        
        # Test invalid message (missing required field)
        invalid_message = self.fix_message.replace(b"55=CDS\x01", b"")
        self.assertFalse(await self.parser.validate(invalid_message))
        
    @pytest.mark.asyncio
    async def test_full_message_parse(self):
        """Test full message parsing through ParserController."""
        message = await self.controller.parse_message(self.fix_message)
        
        # Verify message type
        self.assertIsInstance(message, NewOrderSingleMessage)
        
        # Verify common fields
        self.assertEqual(message.BeginString, "FIX.4.4")
        self.assertEqual(message.MsgType, "D")
        self.assertEqual(message.SenderCompID, "SENDER")
        self.assertEqual(message.TargetCompID, "TARGET")
        
        # Verify CDS-specific fields
        self.assertEqual(message.ClOrdID, "CDS12345")
        self.assertEqual(message.Account, "ACCOUNT123")
        self.assertEqual(message.HandlInst, "1")
        
        # Verify Instrument component
        self.assertIsNotNone(message.Instrument)
        self.assertEqual(message.Instrument.Symbol, "CDS")
        self.assertEqual(message.Instrument.SecurityID, "CDS12345")
        self.assertEqual(message.Instrument.SecurityIDSource, "8")
        self.assertEqual(message.Instrument.SecurityType, "CDS")
        self.assertEqual(message.Instrument.MaturityMonthYear, "202412")
        self.assertEqual(message.Instrument.MaturityDate, datetime(2024, 12, 15).date())
        self.assertEqual(message.Instrument.SecurityExchange, "XCDS")
        self.assertEqual(message.Instrument.Product, 4)  # CDS product type
        
        # Verify OrderQtyData component
        self.assertIsNotNone(message.OrderQtyData)
        self.assertEqual(message.OrderQtyData.OrderQty, 1000000.0)
        
        # Verify other fields
        self.assertEqual(message.OrdType, "2")
        self.assertEqual(message.Price, 100.25)
        self.assertEqual(message.Side, "1")
        self.assertEqual(message.TimeInForce, "0")
        self.assertEqual(message.TransactTime, datetime(2024, 4, 12, 14, 30))
        self.assertEqual(message.PositionEffect, "O")

if __name__ == '__main__':
    unittest.main() 