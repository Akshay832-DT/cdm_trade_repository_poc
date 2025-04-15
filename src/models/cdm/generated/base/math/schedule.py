from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.math.dated_value import DatedValue

class Schedule(CdmModelBase):
    """A class defining a schedule of rates or amounts in terms of an initial value and then a series of step date and value pairs. On each step date the rate or amount changes to the new step value. The series of step date and value pairs are optional. If not specified, this implies that the initial value remains unchanged over time."""
    value: float = Field(description="The initial rate or amount, as the case may be. An initial rate of 5% would be represented as 0.05.")
    dated_value: List[ForwardRef("DatedValue")] = Field(None, description="The schedule of step date and value pairs. On each step date the associated step value becomes effective. A list of steps may be ordered in the document by ascending step date. An FpML document containing an unordered list of steps is still regarded as a conformant document.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.math.dated_value import DatedValue
Schedule.model_rebuild()
