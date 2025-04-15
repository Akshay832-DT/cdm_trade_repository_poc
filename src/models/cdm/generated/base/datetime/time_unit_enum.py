from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class TimeUnitEnum(CdmModelBase):
    """The enumeration values to qualify the allowed units of time."""
    # Enum values
    Day: ClassVar[str] = "Day"
    Hour: ClassVar[str] = "Hour"
    Minute: ClassVar[str] = "Minute"
    Month: ClassVar[str] = "Month"
    Second: ClassVar[str] = "Second"
    Week: ClassVar[str] = "Week"
    Year: ClassVar[str] = "Year"


# Import after class definition to avoid circular imports
TimeUnitEnum.model_rebuild()
