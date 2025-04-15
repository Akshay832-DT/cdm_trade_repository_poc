"""
Test parsing a Credit Default Swap (CDS) CDM JSON message and validate the created objects.
"""
import unittest
import pytest
import json
from datetime import date
from src.parsers.controller import ParserController
from src.parsers.cdm.parser import CdmParser

class TestCdmCreditDefaultSwapMessage(unittest.TestCase):
    """Test cases for Credit Default Swap CDM message parsing."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.parser = CdmParser()
        self.controller = ParserController()
        
        # Example Credit Default Swap CDM message
        self.cdm_message = {
            "TradableProduct": {
                "product": {
                    "TransferableProduct": {
                        "economicTerms": {
                            "payout": [
                                {
                                    "creditDefaultPayout": {
                                        "protectionTerms": {
                                            "creditEvents": [
                                                {"value": "Bankruptcy"},
                                                {"value": "FailureToPay"},
                                                {"value": "Restructuring"}
                                            ],
                                            "obligations": {
                                                "debtType": [
                                                    {"value": "Bond"},
                                                    {"value": "Loan"}
                                                ]
                                            }
                                        },
                                        "payerReceiver": {
                                            "payer": {
                                                "partyReference": {"href": "Party1"}
                                            },
                                            "receiver": {
                                                "partyReference": {"href": "Party2"}
                                            }
                                        },
                                        "referenceInformation": {
                                            "referenceEntity": {
                                                "entityName": {
                                                    "value": "ACME Corporation"
                                                }
                                            },
                                            "referenceObligation": {
                                                "security": {
                                                    "securityType": "Bond",
                                                    "description": {
                                                        "value": "ACME 5.75% 2028"
                                                    }
                                                }
                                            },
                                            "indexReferenceInformation": {
                                                "compositeIndex": {
                                                    "description": {
                                                        "value": "N/A"
                                                    }
                                                }
                                            }
                                        },
                                        "generalTerms": {
                                            "effectiveDate": {
                                                "adjustableDate": {
                                                    "unadjustedDate": "2024-04-15"
                                                }
                                            },
                                            "scheduledTerminationDate": {
                                                "adjustableDate": {
                                                    "unadjustedDate": "2029-04-15"
                                                }
                                            }
                                        },
                                        "feeLeg": {
                                            "paymentFrequency": {
                                                "period": "3M"
                                            },
                                            "fixedAmount": {
                                                "rate": 0.01,
                                                "dayCountFraction": "ACT/360"
                                            }
                                        }
                                    }
                                }
                            ],
                            "effectiveDate": {
                                "adjustableDate": {
                                    "unadjustedDate": "2024-04-15"
                                }
                            },
                            "terminationDate": {
                                "adjustableDate": {
                                    "unadjustedDate": "2029-04-15"
                                }
                            }
                        }
                    }
                },
                "tradableProductIdentifier": {
                    "assignedIdentifier": [
                        {
                            "identifier": {
                                "value": "CDS-2024-001"
                            }
                        }
                    ]
                },
                "tradeDate": {
                    "value": "2024-04-12"
                },
                "tradeIdentifier": [
                    {
                        "issuer": {
                            "value": "Party1"
                        },
                        "assignedIdentifier": [
                            {
                                "identifier": {
                                    "value": "CDS12345"
                                }
                            }
                        ]
                    },
                    {
                        "issuer": {
                            "value": "Party2"
                        },
                        "assignedIdentifier": [
                            {
                                "identifier": {
                                    "value": "CDS67890"
                                }
                            }
                        ]
                    }
                ]
            }
        }
    
    @pytest.mark.asyncio
    async def test_cdm_message_validation(self):
        """Test CDM parser validation."""
        # Convert message to JSON string
        message_str = json.dumps(self.cdm_message)
        
        # Test valid message
        self.assertTrue(await self.parser.validate(message_str))
        
        # Test invalid message (missing required field)
        invalid_message = self.cdm_message.copy()
        del invalid_message["TradableProduct"]["product"]
        invalid_message_str = json.dumps(invalid_message)
        self.assertFalse(await self.parser.validate(invalid_message_str))
    
    @pytest.mark.asyncio
    async def test_full_message_parse(self):
        """Test full message parsing through ParserController."""
        # Convert message to JSON string
        message_str = json.dumps(self.cdm_message)
        
        # Parse message
        message = await self.controller.parse_message(message_str, 'CDM')
        
        # Verify message type
        self.assertEqual(message.__class__.__name__, "TradableProduct")
        
        # Verify product type
        self.assertIsNotNone(message.product.TransferableProduct)
        
        # Verify economic terms
        economic_terms = message.product.TransferableProduct.economicTerms
        self.assertEqual(len(economic_terms.payout), 1)
        
        # Verify credit default payout
        cds_payout = economic_terms.payout[0].creditDefaultPayout
        
        # Verify protection terms
        self.assertEqual(len(cds_payout.protectionTerms.creditEvents), 3)
        self.assertEqual(cds_payout.protectionTerms.creditEvents[0].value, "Bankruptcy")
        self.assertEqual(cds_payout.protectionTerms.creditEvents[1].value, "FailureToPay")
        self.assertEqual(cds_payout.protectionTerms.creditEvents[2].value, "Restructuring")
        
        # Verify payer/receiver
        self.assertEqual(cds_payout.payerReceiver.payer.partyReference.href, "Party1")
        self.assertEqual(cds_payout.payerReceiver.receiver.partyReference.href, "Party2")
        
        # Verify reference information
        self.assertEqual(cds_payout.referenceInformation.referenceEntity.entityName.value, "ACME Corporation")
        self.assertEqual(cds_payout.referenceInformation.referenceObligation.security.description.value, "ACME 5.75% 2028")
        
        # Verify general terms
        self.assertEqual(cds_payout.generalTerms.effectiveDate.adjustableDate.unadjustedDate, "2024-04-15")
        self.assertEqual(cds_payout.generalTerms.scheduledTerminationDate.adjustableDate.unadjustedDate, "2029-04-15")
        
        # Verify fee leg
        self.assertEqual(cds_payout.feeLeg.paymentFrequency.period, "3M")
        self.assertEqual(cds_payout.feeLeg.fixedAmount.rate, 0.01)
        self.assertEqual(cds_payout.feeLeg.fixedAmount.dayCountFraction, "ACT/360")
        
        # Verify trade identifiers
        self.assertEqual(message.tradableProductIdentifier.assignedIdentifier[0].identifier.value, "CDS-2024-001")
        self.assertEqual(message.tradeDate.value, "2024-04-12")
        self.assertEqual(message.tradeIdentifier[0].issuer.value, "Party1")
        self.assertEqual(message.tradeIdentifier[0].assignedIdentifier[0].identifier.value, "CDS12345")
        self.assertEqual(message.tradeIdentifier[1].issuer.value, "Party2")
        self.assertEqual(message.tradeIdentifier[1].assignedIdentifier[0].identifier.value, "CDS67890")

if __name__ == '__main__':
    unittest.main() 