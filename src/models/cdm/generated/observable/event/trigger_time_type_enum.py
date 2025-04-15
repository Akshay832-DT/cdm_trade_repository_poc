from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class TriggerTimeTypeEnum(CdmModelBase):
    """The enumerated values to specify the time of day which would be considered for valuing the knock event."""
    # Enum values
    Anytime: ClassVar[str] = "Anytime"
    Closing: ClassVar[str] = "Closing"


# Import after class definition to avoid circular imports
TriggerTimeTypeEnum.model_rebuild()
