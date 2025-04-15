from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.day_type_enum import DayTypeEnum
    from src.models.cdm.generated.base.datetime.period_enum import PeriodEnum

class Offset(CdmModelBase):
    """A class defining an offset used in calculating a new date relative to a reference date, e.g. calendar days, business days, commodity Business days, etc."""
    period_multiplier: int = Field(None, description="A time period multiplier, e.g. 1, 2 or 3 etc. A negative value can be used when specifying an offset relative to another date, e.g. -2 days.")
    period: ForwardRef("PeriodEnum") = Field(None, description="A time period, e.g. a day, week, month or year of the stream. If the periodMultiplier value is 0 (zero) then period must contain the value D (day).")
    day_type: ForwardRef("DayTypeEnum") = Field(None, description="In the case of an offset specified as a number of days, this element defines whether consideration is given as to whether a day is a good business day or not. If a day type of business days is specified then non-business days are ignored when calculating the offset. The financial business centers to use for determination of business days are implied by the context in which this element is used. This element must only be included when the offset is specified as a number of days. If the offset is zero days then the dayType element should not be included.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.day_type_enum import DayTypeEnum
from src.models.cdm.generated.base.datetime.period_enum import PeriodEnum
Offset.model_rebuild()
