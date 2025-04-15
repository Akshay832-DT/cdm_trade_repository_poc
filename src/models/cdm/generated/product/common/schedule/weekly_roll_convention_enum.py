from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class WeeklyRollConventionEnum(CdmModelBase):
    """The enumerated values to specify the weekly roll day."""
    # Enum values
    FRI: ClassVar[str] = "FRI"
    MON: ClassVar[str] = "MON"
    SAT: ClassVar[str] = "SAT"
    SUN: ClassVar[str] = "SUN"
    TBILL: ClassVar[str] = "TBILL"
    THU: ClassVar[str] = "THU"
    TUE: ClassVar[str] = "TUE"
    WED: ClassVar[str] = "WED"


# Import after class definition to avoid circular imports
WeeklyRollConventionEnum.model_rebuild()
