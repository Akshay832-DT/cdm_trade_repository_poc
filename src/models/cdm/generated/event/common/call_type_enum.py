from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CallTypeEnum(CdmModelBase):
    """Represents the enumeration values that indicate the intended status of message type, such as expected call, notification of a call or a margin call."""
    # Enum values
    ExpectedCall: ClassVar[str] = "ExpectedCall"
    MarginCall: ClassVar[str] = "MarginCall"
    Notification: ClassVar[str] = "Notification"


# Import after class definition to avoid circular imports
CallTypeEnum.model_rebuild()
