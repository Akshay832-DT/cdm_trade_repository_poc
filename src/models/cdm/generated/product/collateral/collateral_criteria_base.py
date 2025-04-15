from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.counterparty_role_enum import CounterpartyRoleEnum
    from src.models.cdm.generated.product.collateral.collateral_criteria import CollateralCriteria
    from src.models.cdm.generated.product.collateral.collateral_margin_type_enum import CollateralMarginTypeEnum
    from src.models.cdm.generated.product.collateral.rating_priority_resolution_enum import RatingPriorityResolutionEnum

class CollateralCriteriaBase(CdmModelBase):
    """Represents a set of criteria used to specify and describe collateral."""
    collateral_criteria: ForwardRef("CollateralCriteria") = Field(description="The specific criteria that applies. It can be created using AND, OR and NOT logic, and both asset and issuer characteristics.")
    applies_to: List[ForwardRef("CounterpartyRoleEnum")] = Field(None, description="Specifies which of the two counterparties the criteria applies to (either one or both counterparties). This attribute is optional, in case the applicable party is already specified elsewhere within a party election.")
    restrict_to: ForwardRef("CollateralMarginTypeEnum") = Field(None, description="Restrict the criteria to only apply to a specific type of margin, ie IM or VM.")
    rating_priority_resolution: ForwardRef("RatingPriorityResolutionEnum") = Field(None, description="Denotes which Criteria has priority if more than one agency rating applies.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.counterparty_role_enum import CounterpartyRoleEnum
from src.models.cdm.generated.product.collateral.collateral_criteria import CollateralCriteria
from src.models.cdm.generated.product.collateral.collateral_margin_type_enum import CollateralMarginTypeEnum
from src.models.cdm.generated.product.collateral.rating_priority_resolution_enum import RatingPriorityResolutionEnum
CollateralCriteriaBase.model_rebuild()
