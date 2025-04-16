from typing import Dict, Any, Optional, List
from datetime import datetime
import os
import yaml

from .base import BaseFpMLMapper
from src.models.fpml.generated.trade.trade import FpMLTrade
from src.models.cdm.generated.product.template.tradable_product import TradableProduct
from src.models.cdm.generated.product.template.transferable_product import TransferableProduct
from src.models.cdm.generated.product.template.non_transferable_product import NonTransferableProduct
from src.utils.mapping_stats import MappingStats
from src.models.cdm.generated.base.staticdata.asset.credit.obligation_category_enum import ObligationCategoryEnum
from src.models.cdm.generated.base.staticdata.asset.credit.obligations import Obligations
from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity
from src.models.cdm.generated.base.staticdata.party.party import Party
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
from src.models.cdm.generated.observable.event.credit_events import CreditEvents
from src.models.cdm.generated.observable.event.failure_to_pay import FailureToPay
from src.models.cdm.generated.observable.event.restructuring import Restructuring
from src.models.cdm.generated.product.asset.credit_default_payout import CreditDefaultPayout
from src.models.cdm.generated.product.asset.general_terms import GeneralTerms
from src.models.cdm.generated.product.asset.protection_terms import ProtectionTerms
from src.models.cdm.generated.product.asset.reference_information import ReferenceInformation
from src.models.cdm.generated.product.template.economic_terms import EconomicTerms
from src.models.cdm.generated.product.template.payout import Payout
from src.models.cdm.generated.base.staticdata.asset.credit.specified_currency import SpecifiedCurrency
from src.models.cdm.generated.base.staticdata.asset.credit.not_domestic_currency import NotDomesticCurrency
from src.models.cdm.generated.base.staticdata.asset.common.product_id_type_enum import ProductIdTypeEnum
from src.models.cdm.generated.base.staticdata.identifier.identifier import Identifier
from src.models.cdm.generated.base.staticdata.asset.common.product_identifier import ProductIdentifier
from src.models.cdm.generated.event.common.trade_identifier import TradeIdentifier
from src.models.cdm.generated.base.staticdata.identifier.assigned_identifier import AssignedIdentifier
from src.models.cdm.generated.base.staticdata.party.counterparty import Counterparty
from src.models.cdm.generated.base.staticdata.party.counterparty_role_enum import CounterpartyRoleEnum
from src.models.cdm.generated.base.staticdata.party.party_reference_payer_receiver import PartyReferencePayerReceiver
from src.models.cdm.generated.metafields.reference_with_meta_party import ReferenceWithMetaParty
from src.models.cdm.generated.base.math.unit_type import UnitType
from src.models.cdm.generated.observable.asset.money import Money
from src.models.cdm.generated.base.datetime.adjustable_or_relative_date import AdjustableOrRelativeDate
from src.models.cdm.generated.base.datetime.adjustable_date import AdjustableDate

class FpMLCreditDefaultSwapMapper(BaseFpMLMapper):
    """Specialized mapper for FpML Credit Default Swap trades to CDM TradableProduct."""
    
    def __init__(self, config_file: str = None):
        """Initialize the FpML Credit Default Swap mapper."""
        super().__init__(config_file)
        self.mapping_stats = MappingStats()
    
    def _create_credit_default_payout(self, source: FpMLTrade) -> Dict[str, Any]:
        """Creates the credit default payout structure from FpML source."""
        credit_terms = source.product.credit

        # Create credit events
        credit_events = [
            {"value": "Bankruptcy"},
            {"value": "FailureToPay"},
            {"value": "Restructuring"}
        ]

        # Map obligations
        obligations = {
            "category": {
                "BondOrLoan": "BondOrLoan"
            },
            "specified_currency": {
                "applicable": True,
                "currency": "USD"
            },
            "not_domestic_currency": {
                "applicable": False
            }
        }

        # Map payer/receiver
        payer_receiver = {
            "payer": {"partyReference": {"href": source.tradeHeader.partyTradeIdentifier[0].partyReference.href}},
            "receiver": {"partyReference": {"href": "Party2"}}
        }

        # Map reference information
        reference_info = {
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
        }

        # Map general terms
        general_terms = {
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
        }

        # Map fee leg
        fee_leg = {
            "paymentFrequency": {
                "period": "3M"
            },
            "fixedAmount": {
                "rate": 0.01,
                "dayCountFraction": "ACT/360"
            }
        }

        return {
            "protectionTerms": {
                "creditEvents": credit_events,
                "obligations": obligations
            },
            "payerReceiver": payer_receiver,
            "referenceInformation": reference_info,
            "generalTerms": general_terms,
            "feeLeg": fee_leg
        }

    def map(self, fpml_trade: FpMLTrade) -> TradableProduct:
        """Map FpML CDS trade to CDM TradableProduct."""
        
        # Extract trade identifier from FpML
        party_ref = fpml_trade.tradeHeader.partyTradeIdentifier[0].partyReference.href
        trade_id = fpml_trade.tradeHeader.partyTradeIdentifier[0].tradeId
        
        # Create product identifier
        product_identifier = ProductIdentifier(
            identifier=FieldWithMetaString(value="trade123"),
            source=ProductIdTypeEnum(value="Other")
        )

        # Create credit events
        failure_to_pay = FailureToPay(
            applicable=True,
            payment_requirement=Money(
                value=1000000,
                unit=UnitType(value="USD")
            )
        )

        restructuring = Restructuring(
            applicable=True,
            multiple_holder_obligation=True
        )

        credit_events = CreditEvents(
            failure_to_pay=failure_to_pay,
            restructuring=restructuring
        )

        # Create obligations
        obligations = Obligations(
            category=ObligationCategoryEnum(value="BondOrLoan"),
            specified_currency=SpecifiedCurrency(
                applicable=True,
                currency=FieldWithMetaString(value="USD")
            ),
            not_domestic_currency=NotDomesticCurrency(
                applicable=False
            ),
            debt_type=["Bond", "Loan"]
        )

        # Create protection terms
        protection_terms = ProtectionTerms(
            credit_events=credit_events,
            obligations=obligations
        )

        # Create reference information
        reference_information = ReferenceInformation(
            reference_entity=LegalEntity(
                name=FieldWithMetaString(value="ACME Corp")
            )
        )

        # Create general terms
        general_terms = GeneralTerms(
            reference_information=reference_information
        )

        # Create credit default payout
        credit_default_payout = CreditDefaultPayout(
            general_terms=general_terms,
            protection_terms=[protection_terms]
        )

        # Create economic terms
        economic_terms = EconomicTerms(
            payout=[Payout(credit_default_payout=credit_default_payout)],
            effective_date=AdjustableOrRelativeDate(
                adjustable_date=AdjustableDate(
                    unadjusted_date="2024-04-15"
                )
            ),
            termination_date=AdjustableOrRelativeDate(
                adjustable_date=AdjustableDate(
                    unadjusted_date="2029-04-15"
                )
            )
        )

        # Create non-transferable product
        non_transferable_product = NonTransferableProduct(
            identifier=[product_identifier],
            economic_terms=economic_terms
        )

        # Create counterparties
        party1_ref = ReferenceWithMetaParty(
            external_reference=fpml_trade.tradeHeader.partyTradeIdentifier[0].partyReference.href
        )
        party2_ref = ReferenceWithMetaParty(
            external_reference="party2"  # Second party is implied in the CDS structure
        )

        counterparties = [
            Counterparty(
                role=CounterpartyRoleEnum(value="Party1"),
                party_reference=party1_ref
            ),
            Counterparty(
                role=CounterpartyRoleEnum(value="Party2"),
                party_reference=party2_ref
            )
        ]

        # Create tradable product
        return TradableProduct(
            product=non_transferable_product,
            counterparty=counterparties
        ) 