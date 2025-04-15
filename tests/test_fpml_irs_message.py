"""
Test parsing an Interest Rate Swap (IRS) FpML message and validate the created objects.
"""
import unittest
import pytest
import asyncio
from datetime import datetime, date
from src.parsers.controller import ParserController
from src.parsers.fpml.parser import FpMLParser
from src.models.fpml.generated.trade import FpMLTrade

class TestInterestRateSwapMessage(unittest.TestCase):
    """Test cases for Interest Rate Swap FpML message parsing."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.parser = FpMLParser()
        self.controller = ParserController()
        
        # Example Interest Rate Swap FpML message
        self.fpml_message = """
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
    
    @pytest.mark.asyncio
    async def test_fpml_message_validation(self):
        """Test FpML parser validation."""
        # Test valid message
        self.assertTrue(await self.parser.validate(self.fpml_message))
        
        # Test invalid message (missing required field)
        invalid_message = self.fpml_message.replace("<tradeDate>2024-04-12</tradeDate>", "")
        self.assertFalse(await self.parser.validate(invalid_message))
    
    @pytest.mark.asyncio
    async def test_full_message_parse(self):
        """Test full message parsing through ParserController."""
        message = await self.controller.parse_message(self.fpml_message, 'FPML')
        
        # Verify message type
        self.assertIsInstance(message, FpMLTrade)
        
        # Verify trade header fields
        self.assertEqual(len(message.tradeHeader.partyTradeIdentifier), 2)
        self.assertEqual(message.tradeHeader.partyTradeIdentifier[0].partyReference.href, "Party1")
        self.assertEqual(message.tradeHeader.partyTradeIdentifier[0].tradeId, "TRADE123")
        self.assertEqual(message.tradeHeader.partyTradeIdentifier[1].partyReference.href, "Party2")
        self.assertEqual(message.tradeHeader.partyTradeIdentifier[1].tradeId, "TRADE456")
        self.assertEqual(message.tradeHeader.tradeDate, date(2024, 4, 12))
        
        # Verify product fields - interest rate swap
        self.assertIsNotNone(message.product.interestRate)
        
        # Verify swap streams
        swap_streams = message.product.interestRate.swapStream
        self.assertEqual(len(swap_streams), 2)
        
        # First stream (fixed leg)
        self.assertEqual(swap_streams[0].payerReceiver.payerPartyReference.href, "Party1")
        self.assertEqual(swap_streams[0].payerReceiver.receiverPartyReference.href, "Party2")
        self.assertEqual(swap_streams[0].paymentFrequency, "Quarterly")
        self.assertEqual(swap_streams[0].notionalAmount.amount, 10000000)
        self.assertEqual(swap_streams[0].notionalAmount.currency, "USD")
        
        # Second stream (floating leg)
        self.assertEqual(swap_streams[1].payerReceiver.payerPartyReference.href, "Party2")
        self.assertEqual(swap_streams[1].payerReceiver.receiverPartyReference.href, "Party1")
        self.assertEqual(swap_streams[1].paymentFrequency, "Quarterly")
        self.assertEqual(swap_streams[1].notionalAmount.amount, 10000000)
        self.assertEqual(swap_streams[1].notionalAmount.currency, "USD")

if __name__ == '__main__':
    unittest.main() 