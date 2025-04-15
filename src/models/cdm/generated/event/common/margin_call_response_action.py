from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.common.collateral_position import CollateralPosition
    from src.models.cdm.generated.event.common.margin_call_action_enum import MarginCallActionEnum

class MarginCallResponseAction(CdmModelBase):
    """Specifies the margin call action details, including collateral to be moved and its direction."""
    collateral_position_component: List[ForwardRef("CollateralPosition")] = Field(None, description="Specifies the collateral to be moved and its direction.")
    margin_call_action: ForwardRef("MarginCallActionEnum") = Field(description="Specifies the margin call action details, specified as either Delivery or Return.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.common.collateral_position import CollateralPosition
from src.models.cdm.generated.event.common.margin_call_action_enum import MarginCallActionEnum
MarginCallResponseAction.model_rebuild()
