from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.collateral.collateral_type_enum import CollateralTypeEnum
    from src.models.cdm.generated.product.collateral.eligible_collateral_criteria import EligibleCollateralCriteria
    from src.models.cdm.generated.product.collateral.substitution_provisions import SubstitutionProvisions

class CollateralProvisions(CdmModelBase):
    """Contains collateral attributes which can also inherit information from a GMRA"""
    collateral_type: ForwardRef("CollateralTypeEnum") = Field(description="Enumerates the collateral types which are accepted by the Seller.")
    eligible_collateral: List[ForwardRef("EligibleCollateralCriteria")] = Field(None, description="The eligible collateral as specified in relation to the transaction.")
    substitution_provisions: ForwardRef("SubstitutionProvisions") = Field(None, description="The provisions for collateral substitutions such as how many and when they are allowed.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.collateral.collateral_type_enum import CollateralTypeEnum
from src.models.cdm.generated.product.collateral.eligible_collateral_criteria import EligibleCollateralCriteria
from src.models.cdm.generated.product.collateral.substitution_provisions import SubstitutionProvisions
CollateralProvisions.model_rebuild()
