from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.adjustable_or_relative_date import AdjustableOrRelativeDate
    from src.models.cdm.generated.base.datetime.business_day_adjustments import BusinessDayAdjustments
    from src.models.cdm.generated.base.datetime.calculation_period_frequency import CalculationPeriodFrequency
    from src.models.cdm.generated.base.datetime.day_type_enum import DayTypeEnum

class PeriodicDates(CdmModelBase):
    """A class for specifying a calculation period schedule."""
    start_date: ForwardRef("AdjustableOrRelativeDate") = Field(None, description="The start date of the calculation period. FpML specifies that for interest rate swaps this date must only be specified if it is not equal to the effective date. It is always specified in the case of equity swaps and credit default swaps with periodic payments. This date may be subject to adjustment in accordance with a business day convention.")
    end_date: ForwardRef("AdjustableOrRelativeDate") = Field(None, description="The end date of the calculation period. FpML specifies that for interest rate swaps this date must only be specified if it is not equal to the termination date. It is always specified in the case of equity swaps with periodic payments. This date may be subject to adjustment in accordance with a business day convention.")
    period_frequency: ForwardRef("CalculationPeriodFrequency") = Field(None, description="The frequency at which calculation period end dates occur with the regular part of the calculation period schedule and their roll date convention.")
    period_dates_adjustments: ForwardRef("BusinessDayAdjustments") = Field(None, description="The specification of the business day convention and financial business centers used for adjusting any calculation period date if it would otherwise fall on a day that is not a business day in the specified business center.")
    day_type: ForwardRef("DayTypeEnum") = Field(None, description="Denotes the enumerated values to specify the day type classification used in counting the number of days between two dates.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.adjustable_or_relative_date import AdjustableOrRelativeDate
from src.models.cdm.generated.base.datetime.business_day_adjustments import BusinessDayAdjustments
from src.models.cdm.generated.base.datetime.calculation_period_frequency import CalculationPeriodFrequency
from src.models.cdm.generated.base.datetime.day_type_enum import DayTypeEnum
PeriodicDates.model_rebuild()
