import pytest
import json
import os
from src.mappers.fpml.credit_default_swap_mapper import FpMLCreditDefaultSwapMapper
from src.models.fpml.generated.trade.trade import (
    FpMLTrade, Product, CreditProduct, ProtectionTerms,
    ReferenceInformation, TradeHeader, PartyTradeIdentifier,
    PartyReference
)
from datetime import date
from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
from src.models.cdm.generated.product.asset.reference_obligation import ReferenceObligation
from src.models.cdm.generated.base.staticdata.asset.common.security import Security
from src.models.cdm.generated.base.staticdata.asset.common.product_id_type_enum import ProductIdTypeEnum

class TestCreditDefaultSwapMapper:
    """Test cases for the FpML Credit Default Swap Mapper."""
    
    @pytest.fixture
    def cds_mapper(self):
        """Initialize the CDS mapper fixture."""
        return FpMLCreditDefaultSwapMapper()
    
    @pytest.fixture
    def sample_fpml_cds(self):
        """Sample FpML CDS trade."""
        # Create a LegalEntity for ACME Corp (only used in CDM output)
        acme_corp = LegalEntity(
            name=FieldWithMetaString(value="ACME Corp")
        )
        
        # Create a Security for Bond-123 (only used in CDM output)
        bond_123 = Security(
            productIdentifier=[FieldWithMetaString(value="Bond-123")],
            securityType="Bond"
        )
        
        # Create a ReferenceObligation (only used in CDM output)
        ref_obligation = ReferenceObligation(
            security=bond_123
        )
        
        return FpMLTrade(
            tradeHeader=TradeHeader(
                partyTradeIdentifier=[
                    PartyTradeIdentifier(
                        partyReference=PartyReference(**{"@href": "party1"}),
                        tradeId="trade123"
                    )
                ],
                tradeDate=date(2024, 1, 1)
            ),
            product=Product(
                credit=CreditProduct(
                    protectionTerms=ProtectionTerms(
                        referenceEntity="ACME Corp",  # Use string for FpML
                        creditEvent="Default",
                        settlementType="Physical"
                    ),
                    referenceInformation=ReferenceInformation(
                        referenceEntity="ACME Corp",  # Use string for FpML
                        referenceObligation="Bond-123"  # Use string for FpML
                    )
                )
            )
        )
    
    def test_mapper_initializes_properly(self, cds_mapper):
        """Test that the mapper initializes correctly."""
        assert cds_mapper is not None
        assert hasattr(cds_mapper, "mapping_stats")
    
    def test_credit_default_swap_mapping(self, cds_mapper, sample_fpml_cds):
        """Test the mapping of a sample CDS trade."""
        # Map the sample FpML CDS trade to CDM
        result = cds_mapper.map(sample_fpml_cds)
        
        # Verify the result is not None
        assert result is not None
        
        # Verify product identifiers
        assert len(result.product.identifier) == 1
        assert result.product.identifier[0].identifier.value == "trade123"
        assert result.product.identifier[0].source.value == "Other"
        
        # Verify economic terms
        economic_terms = result.product.economic_terms
        assert economic_terms.effective_date.adjustable_date.unadjusted_date == "2024-04-15"
        assert economic_terms.termination_date.adjustable_date.unadjusted_date == "2029-04-15"
        
        # Verify credit default payout
        credit_payout = economic_terms.payout[0].credit_default_payout
        
        # Verify protection terms
        protection_terms = credit_payout.protection_terms[0]
        assert protection_terms.credit_events.failure_to_pay.applicable is True
        assert protection_terms.credit_events.failure_to_pay.payment_requirement.value == 1000000
        assert protection_terms.credit_events.failure_to_pay.payment_requirement.unit.value == "USD"
        assert protection_terms.credit_events.restructuring.applicable is True
        assert protection_terms.credit_events.restructuring.multiple_holder_obligation is True
        
        # Verify obligations
        assert protection_terms.obligations.category.value == "BondOrLoan"
        assert protection_terms.obligations.specified_currency.applicable is True
        assert protection_terms.obligations.specified_currency.currency.value == "USD"
        assert protection_terms.obligations.not_domestic_currency.applicable is False
        assert protection_terms.obligations.debt_type == ["Bond", "Loan"]
        
        # Verify counterparties
        assert len(result.counterparty) == 2
        assert result.counterparty[0].role.value == "Party1"
        assert result.counterparty[0].party_reference is not None
        assert result.counterparty[1].role.value == "Party2"
        assert result.counterparty[1].party_reference is not None 