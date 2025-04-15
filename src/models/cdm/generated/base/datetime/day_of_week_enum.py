from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class DayOfWeekEnum(CdmModelBase):
    """The enumerated values to specify a day of the seven-day week."""
    # Enum values
    FRI: ClassVar[str] = "FRI"
    MON: ClassVar[str] = "MON"
    SAT: ClassVar[str] = "SAT"
    SUN: ClassVar[str] = "SUN"
    THU: ClassVar[str] = "THU"
    TUE: ClassVar[str] = "TUE"
    WED: ClassVar[str] = "WED"


# Import after class definition to avoid circular imports
DayOfWeekEnum.model_rebuild()
