from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.collateral.eligible_collateral_criteria import EligibleCollateralCriteria

class EligibleCollateralSpecificationInstruction(CdmModelBase):
    """"""
    common: ForwardRef("EligibleCollateralCriteria") = Field()
    variable: List[ForwardRef("EligibleCollateralCriteria")] = Field(None)

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.collateral.eligible_collateral_criteria import EligibleCollateralCriteria
EligibleCollateralSpecificationInstruction.model_rebuild()
