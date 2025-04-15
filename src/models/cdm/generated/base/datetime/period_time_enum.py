from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class PeriodTimeEnum(CdmModelBase):
    """The enumeration values to specify a time period containing additional values such as Term."""
    # Enum values
    Hour: ClassVar[str] = "Hour"
    Minute: ClassVar[str] = "Minute"
    Second: ClassVar[str] = "Second"


# Import after class definition to avoid circular imports
PeriodTimeEnum.model_rebuild()
