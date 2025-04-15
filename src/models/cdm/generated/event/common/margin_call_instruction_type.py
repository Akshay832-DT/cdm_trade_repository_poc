from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.common.call_type_enum import CallTypeEnum

class MarginCallInstructionType(CdmModelBase):
    """Represents enumeration values to specify the call notification type, direction, specific action type."""
    call_type: ForwardRef("CallTypeEnum") = Field(description="Indicates the status of the call message type, such as expected call, notification of a call or an actionable margin call.")
    visibility_indicator: bool = Field(None, description="Indicates the choice if the call instruction is visible or not to the other party.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.common.call_type_enum import CallTypeEnum
MarginCallInstructionType.model_rebuild()
