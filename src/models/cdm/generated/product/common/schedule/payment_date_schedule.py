from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.adjustable_or_relative_date import AdjustableOrRelativeDate
    from src.models.cdm.generated.base.datetime.adjustable_relative_or_periodic_dates import AdjustableRelativeOrPeriodicDates

class PaymentDateSchedule(CdmModelBase):
    """The payment dates when specified as relative to a set of dates specified somewhere else in the instance document/transaction, e.g. the valuation dates as typically the case for equity swaps, or when specified as a calculation period schedule."""
    interim_payment_dates: List[ForwardRef("AdjustableRelativeOrPeriodicDates")] = Field(None)
    final_payment_date: ForwardRef("AdjustableOrRelativeDate") = Field(None, description="The last payment when specified as an adjustable or relative date, as in the FpML total return construct.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.adjustable_or_relative_date import AdjustableOrRelativeDate
from src.models.cdm.generated.base.datetime.adjustable_relative_or_periodic_dates import AdjustableRelativeOrPeriodicDates
PaymentDateSchedule.model_rebuild()
