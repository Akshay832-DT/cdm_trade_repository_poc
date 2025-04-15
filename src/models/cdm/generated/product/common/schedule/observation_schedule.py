from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.business_day_adjustments import BusinessDayAdjustments
    from src.models.cdm.generated.product.common.schedule.observation_date import ObservationDate

class ObservationSchedule(CdmModelBase):
    """Specifies a single date on which market observations take place and specifies optional associated weighting."""
    observation_date: List[ForwardRef("ObservationDate")] = Field(None, description="Specifies an adjusted or unadjusted date for a market observation.")
    date_adjustments: ForwardRef("BusinessDayAdjustments") = Field(None, description="The business day convention and financial business centers used for adjusting the date if it would otherwise fall on a day that is not a business date in the specified business centers.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.business_day_adjustments import BusinessDayAdjustments
from src.models.cdm.generated.product.common.schedule.observation_date import ObservationDate
ObservationSchedule.model_rebuild()
