from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.period_extended_enum import PeriodExtendedEnum

class Frequency(CdmModelBase):
    """A class for defining a date frequency, e.g. one day, three months, through the combination of an integer value and a standardized period value that is specified as part of an enumeration."""
    period_multiplier: int = Field(description="A time period multiplier, e.g. 1, 2, or 3. If the period value is T (Term) then period multiplier must contain the value 1.")
    period: ForwardRef("PeriodExtendedEnum") = Field(description="A time period, e.g. a day, week, month, year or term of the stream.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.period_extended_enum import PeriodExtendedEnum
Frequency.model_rebuild()
