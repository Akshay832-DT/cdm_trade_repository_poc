from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.period import Period

class ExercisePeriod(CdmModelBase):
    """This defines the time interval to the start of the exercise period, i.e. the earliest exercise date, and the frequency of subsequent exercise dates (if any)."""
    earliest_exercise_date_tenor: ForwardRef("Period") = Field(description="The time interval to the first (and possibly only) exercise date in the exercise period.")
    exercise_frequency: ForwardRef("Period") = Field(None, description="The frequency of subsequent exercise dates in the exercise period following the earliest exercise date. An interval of 1 day should be used to indicate an American style exercise period.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.period import Period
ExercisePeriod.model_rebuild()
