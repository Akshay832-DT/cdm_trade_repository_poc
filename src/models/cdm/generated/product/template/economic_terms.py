from typing import Dict, Any, Optional, List
from pydantic import Field, model_validator

from src.models.cdm.generated.base.base import CdmModelBase
from src.models.cdm.generated.base.datetime.adjustable_or_relative_date import AdjustableOrRelativeDate
from src.models.cdm.generated.base.datetime.business_day_adjustments import BusinessDayAdjustments
from src.models.cdm.generated.product.template.payout import Payout

class EconomicTerms(CdmModelBase):
    """The economic terms of a product."""
    
    effective_date: Optional[Dict[str, Any]] = Field(None, alias="effectiveDate", description="The effective date of the product.")
    termination_date: Optional[Dict[str, Any]] = Field(None, alias="terminationDate", description="The termination date of the product.")
    date_adjustments: Optional[Dict[str, Any]] = Field(None, alias="dateAdjustments", description="The date adjustments for the product.")
    payout: List[Dict[str, Any]] = Field(default_factory=list, description="The payout terms of the product.")
    termination_provision: Optional[Dict[str, Any]] = Field(None, alias="terminationProvision", description="The termination provision of the product.")
    calculation_agent: Optional[Dict[str, Any]] = Field(None, alias="calculationAgent", description="The calculation agent of the product.")
    non_standardised_terms: Optional[Dict[str, Any]] = Field(None, alias="nonStandardisedTerms", description="The non-standardised terms of the product.")
    collateral: Optional[Dict[str, Any]] = Field(None, description="The collateral terms of the product.")
    
    @model_validator(mode='after')
    def validate_types(self) -> 'EconomicTerms':
        """Validate that the types of the attributes are correct."""
        try:
            if self.effective_date:
                self.effective_date = AdjustableOrRelativeDate(**self.effective_date)
            if self.termination_date:
                self.termination_date = AdjustableOrRelativeDate(**self.termination_date)
            if self.date_adjustments:
                self.date_adjustments = BusinessDayAdjustments(**self.date_adjustments)
            
            # Handle empty payout list gracefully
            if self.payout:
                validated_payouts = []
                for payout in self.payout:
                    if isinstance(payout, dict):
                        validated_payouts.append(Payout(**payout))
                    elif isinstance(payout, Payout):
                        validated_payouts.append(payout)
                    else:
                        raise ValueError(f"Invalid payout type: {type(payout)}")
                self.payout = validated_payouts
            
        except Exception as e:
            raise ValueError(f"Failed to validate EconomicTerms: {str(e)}")
        return self

EconomicTerms.model_rebuild()
