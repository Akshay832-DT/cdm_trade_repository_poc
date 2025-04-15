from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.collateral.eligibility_query import EligibilityQuery
    from src.models.cdm.generated.product.collateral.eligible_collateral_criteria import EligibleCollateralCriteria
    from src.models.cdm.generated.product.collateral.eligible_collateral_specification import EligibleCollateralSpecification

class CheckEligibilityResult(CdmModelBase):
    """Result for the CheckEligibilityByDetails and CheckEligibilityForProduct functions"""
    is_eligible: bool = Field(description="a simple boolean which is set to true if the asset described in the EligibilityQuery input is eligible")
    matching_eligible_criteria: List[ForwardRef("EligibleCollateralCriteria")] = Field(None, description="if there was a match, this will be the one or more criteria that were supplied in the EligbilityCollateralSpecification which matched with the query input")
    eligibility_query: ForwardRef("EligibilityQuery") = Field(description="a copy of the input query that was checked against the eligible collateral specification")
    specification: ForwardRef("EligibleCollateralSpecification") = Field(description="a copy of the input EligbilityCollateralSpecification that was checked against the query")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.collateral.eligibility_query import EligibilityQuery
from src.models.cdm.generated.product.collateral.eligible_collateral_criteria import EligibleCollateralCriteria
from src.models.cdm.generated.product.collateral.eligible_collateral_specification import EligibleCollateralSpecification
CheckEligibilityResult.model_rebuild()
