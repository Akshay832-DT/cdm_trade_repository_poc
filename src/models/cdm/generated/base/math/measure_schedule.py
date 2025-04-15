from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.math.dated_value import DatedValue
    from src.models.cdm.generated.base.math.unit_type import UnitType

class MeasureSchedule(CdmModelBase):
    """A set of measures, all in the same unit, where the values are defined through a schedule of steps. The initial value may be defined either as part of the steps, or using the single amount attribute."""
    value: float = Field(None, description="Specifies the value of the measure as a number. Optional because in a measure vector or schedule, this single value may be omitted.")
    unit: ForwardRef("UnitType") = Field(None, description="Qualifies the unit by which the amount is measured. Optional because a measure may be unit-less (e.g. when representing a ratio between amounts in the same unit).")
    dated_value: List[ForwardRef("DatedValue")] = Field(None, description="A schedule of step date and value pairs. On each step date the associated step value becomes effective. The step dates are used to order the steps by ascending order. This attribute is optional so the data type may be used to define a schedule with a single value.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.math.dated_value import DatedValue
from src.models.cdm.generated.base.math.unit_type import UnitType
MeasureSchedule.model_rebuild()
