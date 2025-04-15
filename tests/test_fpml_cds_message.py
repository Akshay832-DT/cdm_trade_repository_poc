"""
Test parsing a Credit Default Swap (CDS) FpML message and validate the created objects.
"""
import unittest
import pytest
import asyncio
from datetime import datetime, date
from src.parsers.controller import ParserController
from src.parsers.fpml.parser import FpMLParser
from src.models.fpml.generated.trade import FpMLTrade

class TestCreditDefaultSwapMessage(unittest.TestCase):
    """Test cases for Credit Default Swap FpML message parsing."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.parser = FpMLParser()
        self.controller = ParserController()
        
        # Example Credit Default Swap FpML message
        self.fpml_message = """
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
    
    @pytest.mark.asyncio
    async def test_fpml_message_validation(self):
        """Test FpML parser validation."""
        # Test valid message
        self.assertTrue(await self.parser.validate(self.fpml_message))
        
        # Test invalid message (missing required field)
        invalid_message = self.fpml_message.replace("<referenceEntity>ACME Corporation</referenceEntity>", "", 1)
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
        self.assertEqual(message.tradeHeader.partyTradeIdentifier[0].tradeId, "CDS12345")
        self.assertEqual(message.tradeHeader.partyTradeIdentifier[1].partyReference.href, "Party2")
        self.assertEqual(message.tradeHeader.partyTradeIdentifier[1].tradeId, "CDS67890")
        self.assertEqual(message.tradeHeader.tradeDate, date(2024, 4, 12))
        
        # Verify product fields - credit default swap
        self.assertIsNotNone(message.product.credit)
        self.assertIsNone(message.product.interestRate)
        
        # Verify protection terms
        self.assertEqual(message.product.credit.protectionTerms.referenceEntity, "ACME Corporation")
        self.assertEqual(message.product.credit.protectionTerms.creditEvent, "Bankruptcy")
        self.assertEqual(message.product.credit.protectionTerms.settlementType, "Physical")
        
        # Verify reference information
        self.assertEqual(message.product.credit.referenceInformation.referenceEntity, "ACME Corporation")
        self.assertEqual(message.product.credit.referenceInformation.referenceObligation, "ACME 5.75% 2028")

if __name__ == '__main__':
    unittest.main() 