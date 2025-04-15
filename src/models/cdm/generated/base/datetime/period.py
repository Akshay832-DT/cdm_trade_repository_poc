from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.period_enum import PeriodEnum

class Period(CdmModelBase):
    """A class to define recurring periods or time offsets."""
    period_multiplier: int = Field(description="A time period multiplier, e.g. 1, 2 or 3 etc. A negative value can be used when specifying an offset relative to another date, e.g. -2 days.")
    period: ForwardRef("PeriodEnum") = Field(description="A time period, e.g. a day, week, month or year of the stream. If the periodMultiplier value is 0 (zero) then period must contain the value D (day).")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.period_enum import PeriodEnum
Period.model_rebuild()
