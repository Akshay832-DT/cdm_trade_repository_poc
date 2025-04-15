from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.periodic_dates import PeriodicDates
    from src.models.cdm.generated.product.common.schedule.observation_schedule import ObservationSchedule
    from src.models.cdm.generated.product.common.schedule.parametric_dates import ParametricDates

class ObservationDates(CdmModelBase):
    """Describes date details for a set of observation dates in parametric or non-parametric form."""
    observation_schedule: ForwardRef("ObservationSchedule") = Field(None, description="Specifies a schedule of dates (non-parametric) on which market observations take place, and allows for the optional definition of weights where applicable.  When no weight is specified, then weight of each date is assumed to be 1.0")
    periodic_schedule: ForwardRef("PeriodicDates") = Field(None, description="Specifies the date range and frequency on which market observations take place.  Weights can be assigned to dates in the schedule by assigning the weight and corresponding observationReference in the observationSchedule.")
    parametric_dates: ForwardRef("ParametricDates") = Field(None, description="Specifies parametric terms to determine which days within a given calculation period the price would be observed. Typically associated with Commodities. ")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.periodic_dates import PeriodicDates
from src.models.cdm.generated.product.common.schedule.observation_schedule import ObservationSchedule
from src.models.cdm.generated.product.common.schedule.parametric_dates import ParametricDates
ObservationDates.model_rebuild()
