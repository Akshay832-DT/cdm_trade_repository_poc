from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class PeriodEnum(CdmModelBase):
    """The enumerated values to specify the period, e.g. day, week."""
    # Enum values
    D: ClassVar[str] = "D"
    M: ClassVar[str] = "M"
    W: ClassVar[str] = "W"
    Y: ClassVar[str] = "Y"


# Import after class definition to avoid circular imports
PeriodEnum.model_rebuild()
