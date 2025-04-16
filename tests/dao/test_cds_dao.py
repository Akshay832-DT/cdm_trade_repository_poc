"""
Test the CDS DAO implementation.
"""
import os
import pytest
import json
import asyncio
from datetime import date

from src.parsers.controller import ParserController
from src.dao.cdm.db_manager import db_manager
from src.dao.cdm.cds_dao import CreditDefaultSwapDAO

class TestCdsDAO:
    """Test the CDS DAO implementation."""
    
    @classmethod
    def setup_class(cls):
        """Set up test fixtures at the class level."""
        # Set up test database connection
        db_manager.host = os.environ.get('TEST_DB_HOST', 'localhost')
        db_manager.port = int(os.environ.get('TEST_DB_PORT', 5432))
        db_manager.database = os.environ.get('TEST_DB_NAME', 'cdm_trade_db_test')
        db_manager.user = os.environ.get('TEST_DB_USER', 'postgres')
        db_manager.password = os.environ.get('TEST_DB_PASSWORD', 'postgres')
        
        # Update connection string
        db_manager.conn_string = (
            f"host={db_manager.host} "
            f"port={db_manager.port} "
            f"dbname={db_manager.database} "
            f"user={db_manager.user} "
            f"password={db_manager.password}"
        )
        
        # Close any existing pool
        if db_manager.pool is not None:
            db_manager.close_pool()
        
        # Initialize pool with test config
        db_manager.initialize_pool(min_size=1, max_size=5)
        
        # Initialize database schema
        schema_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 
                                  'src', 'dao', 'cdm', 'schema.sql')
        loop = asyncio.get_event_loop()
        loop.run_until_complete(db_manager.execute_script(schema_path))
        
        # Initialize DAO
        cls.cds_dao = CreditDefaultSwapDAO()
    
    @pytest.mark.asyncio
    async def test_save_cds_trade(self):
        """Test saving a CDS trade."""
        # Parse a CDM message
        parser = ParserController()
        
        # Example Credit Default Swap CDM message
        cdm_message = {
            "TradableProduct": {
                "product": {
                    "TransferableProduct": {
                        "economicTerms": {
                            "payout": [
                                {
                                    "creditDefaultPayout": {
                                        "protectionTerms": [{
                                            "creditEvents": [
                                                {"value": "Bankruptcy"},
                                                {"value": "FailureToPay"},
                                                {"value": "Restructuring"}
                                            ],
                                            "obligations": {
                                                "category": {
                                                    "value": "BondOrLoan"
                                                },
                                                "debtType": [
                                                    {"value": "Bond"},
                                                    {"value": "Loan"}
                                                ],
                                                "notSubordinated": True,
                                                "specifiedCurrency": {
                                                    "applicable": True,
                                                    "currency": {"value": "USD"}
                                                }
                                            }
                                        }],
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
                                                },
                                                "entityType": "Corporate"
                                            },
                                            "referenceObligation": {
                                                "security": {
                                                    "securityType": "Bond",
                                                    "description": {
                                                        "value": "ACME 5.75% 2028"
                                                    },
                                                    "maturityDate": "2028-06-15",
                                                    "identifiers": {
                                                        "ISIN": "US123456AB12"
                                                    }
                                                }
                                            },
                                            "allGuarantees": True
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
                                            "firstPaymentDate": "2024-07-15",
                                            "lastPaymentDate": "2029-04-15",
                                            "fixedAmount": {
                                                "rate": 0.01,
                                                "dayCountFraction": "ACT/360"
                                            }
                                        },
                                        "priceQuantity": {
                                            "quantity": {
                                                "amount": 10000000,
                                                "unitOfAmount": {
                                                    "currency": {
                                                        "value": "USD"
                                                    }
                                                }
                                            }
                                        },
                                        "settlementTerms": {
                                            "settlementType": {
                                                "value": "Cash"
                                            },
                                            "settlementCurrency": {
                                                "value": "USD"
                                            },
                                            "settlementDate": {
                                                "adjustableDate": {
                                                    "unadjustedDate": "2029-04-20"
                                                }
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
                ],
                "party": [
                    {
                        "id": "Party1",
                        "name": "Bank ABC",
                        "entityType": "Bank"
                    },
                    {
                        "id": "Party2",
                        "name": "Client XYZ",
                        "entityType": "Corporate"
                    }
                ]
            }
        }
        
        message_str = json.dumps(cdm_message)
        parsed_message = await parser.parse_message(message_str, 'CDM')
        
        # Save trade to database
        trade_db_id = self.cds_dao.save(parsed_message)
        
        # Verify trade was saved
        assert trade_db_id is not None
        
        # Get trade from database
        cds = self.cds_dao.get_by_trade_id(trade_db_id)
        assert cds is not None
        
        # Verify CDS details
        assert cds['buy_sell'] == 'BUY'
        assert cds['fixed_rate'] == 0.01
        assert cds['day_count_fraction'] == 'ACT/360'
        assert cds['payment_frequency'] == '3M'
        
        # Get all CDS trades with details
        all_cds = self.cds_dao.get_all_with_details()
        assert len(all_cds) >= 1
        
        # Find our trade in the results
        found = False
        for trade in all_cds:
            if trade['trade_external_id'] == 'CDS12345':
                found = True
                assert trade['reference_entity_name'] == 'ACME Corporation'
                assert trade['reference_obligation_desc'] == 'ACME 5.75% 2028'
                break
        
        assert found
        
        # Get comprehensive details
        comp_details = self.cds_dao.get_comprehensive_details(trade_db_id)
        assert len(comp_details) == 1
        
        # Verify comprehensive details include credit events
        credit_events = comp_details[0]['credit_events']
        assert credit_events is not None
        assert isinstance(credit_events, list) or isinstance(credit_events, dict)
        
    @pytest.mark.asyncio
    async def test_coverage_report(self):
        """Test coverage report generation."""
        report = self.cds_dao.get_coverage_report()
        assert report is not None
        assert report['model'] == 'CreditDefaultSwap'
        assert isinstance(report['implemented_fields'], list)
        assert isinstance(report['coverage_percentage'], int)
        assert report['coverage_percentage'] > 0
        assert 'database_tables' in report 