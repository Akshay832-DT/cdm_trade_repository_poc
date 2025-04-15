from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.common.corporate_action_type_enum import CorporateActionTypeEnum
    from src.models.cdm.generated.product.template.underlier import Underlier

class CorporateAction(CdmModelBase):
    """Specifies the relevant data regarding a corporate action."""
    corporate_action_type: ForwardRef("CorporateActionTypeEnum") = Field(description="The type of corporate action taking place.")
    ex_date: str = Field(description="The date on which the corporate action is known to have taken place.")
    pay_date: str = Field(description="The date on which resulting from the corporate action are delivered.")
    underlier: ForwardRef("Underlier") = Field(description="The underlier impacted by the corporate action.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.common.corporate_action_type_enum import CorporateActionTypeEnum
from src.models.cdm.generated.product.template.underlier import Underlier
CorporateAction.model_rebuild()
