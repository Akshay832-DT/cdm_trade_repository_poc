from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.frequency import Frequency
    from src.models.cdm.generated.base.math.dated_value import DatedValue
    from src.models.cdm.generated.base.math.measure import Measure
    from src.models.cdm.generated.base.math.unit_type import UnitType

class QuantitySchedule(CdmModelBase):
    """Specifies a quantity schedule to be associated to a financial product to represent a trade amount. This data type extends MeasureSchedule with several unit or multiplier attributes that are used to define financial quantities. This data type is generically based on a schedule and can also be used to represent a quantity as a single value."""
    value: float = Field(None, description="Specifies the value of the measure as a number. Optional because in a measure vector or schedule, this single value may be omitted.")
    unit: ForwardRef("UnitType") = Field(None, description="Qualifies the unit by which the amount is measured. Optional because a measure may be unit-less (e.g. when representing a ratio between amounts in the same unit).")
    dated_value: List[ForwardRef("DatedValue")] = Field(None, description="A schedule of step date and value pairs. On each step date the associated step value becomes effective. The step dates are used to order the steps by ascending order. This attribute is optional so the data type may be used to define a schedule with a single value.")
    multiplier: ForwardRef("Measure") = Field(None, description="Defines an optional number that the quantity should be multiplied by to derive a total quantity. This number is associated to a unit. For example in the case of the Coal (API2) CIF ARA (ARGUS-McCloskey) Futures Contract on the CME, where the unit would be contracts, the multiplier value would 1,000 and the mulitiplier unit would be 1,000 MT (Metric Tons).")
    frequency: ForwardRef("Frequency") = Field(None, description="Defines the frequency to be used when defining a quantity. For example a quantity may be specified as a number of barrels of oil per day, which needs multiplying by the number of days in the relevant period to get the total quantity as a number of barrels.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.frequency import Frequency
from src.models.cdm.generated.base.math.dated_value import DatedValue
from src.models.cdm.generated.base.math.measure import Measure
from src.models.cdm.generated.base.math.unit_type import UnitType
QuantitySchedule.model_rebuild()
