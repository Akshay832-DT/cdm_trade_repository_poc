from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class TriggerTypeEnum(CdmModelBase):
    """The enumerated values to specify whether an option will trigger or expire depending upon whether the spot rate is above or below the barrier rate."""
    # Enum values
    Equal: ClassVar[str] = "Equal"
    EqualOrGreater: ClassVar[str] = "EqualOrGreater"
    EqualOrLess: ClassVar[str] = "EqualOrLess"
    Greater: ClassVar[str] = "Greater"
    Less: ClassVar[str] = "Less"


# Import after class definition to avoid circular imports
TriggerTypeEnum.model_rebuild()
