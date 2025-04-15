from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.business_center_enum import BusinessCenterEnum
    from src.models.cdm.generated.base.datetime.business_center_time import BusinessCenterTime
    from src.models.cdm.generated.base.datetime.day_of_week_enum import DayOfWeekEnum
    from src.models.cdm.generated.base.datetime.period import Period

class CalculationFrequency(CdmModelBase):
    """Represents the parameters for describing how often something (such as collateral interest) is to be calculated."""
    period: ForwardRef("Period") = Field(description="Specifies the time period at which calculation is performed, e.g. 1 month.")
    month_of_year: float = Field(None, description="Specifies the month of the year if used.")
    day_of_month: float = Field(None, description="Specifies the day of the month if used.")
    day_of_week: ForwardRef("DayOfWeekEnum") = Field(None, description="Specifies the day of the week if used.")
    week_of_month: float = Field(None, description="Specifies the week of the month if used.")
    offset_days: float = Field(description="Specifies how many days from the trigger event should the payment occur.")
    date_location: ForwardRef("BusinessCenterTime") = Field(description="Specifies where is the time measured.")
    business_center: List[ForwardRef("BusinessCenterEnum")] = Field(None, description="Specifies the business center for adjustment of calculation period.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.business_center_enum import BusinessCenterEnum
from src.models.cdm.generated.base.datetime.business_center_time import BusinessCenterTime
from src.models.cdm.generated.base.datetime.day_of_week_enum import DayOfWeekEnum
from src.models.cdm.generated.base.datetime.period import Period
CalculationFrequency.model_rebuild()
