from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.adjustable_or_relative_date import AdjustableOrRelativeDate
    from src.models.cdm.generated.base.datetime.business_day_adjustments import BusinessDayAdjustments
    from src.models.cdm.generated.base.datetime.calculation_period_frequency import CalculationPeriodFrequency
    from src.models.cdm.generated.product.common.schedule.stub_period_type_enum import StubPeriodTypeEnum

class CalculationPeriodDates(CdmModelBase):
    """A data for:  defining the parameters used to generate the calculation period dates schedule, including the specification of any initial or final stub calculation periods. A calculation period schedule consists of an optional initial stub calculation period, one or more regular calculation periods and an optional final stub calculation period. In the absence of any initial or final stub calculation periods, the regular part of the calculation period schedule is assumed to be between the effective date and the termination date. No implicit stubs are allowed, i.e. stubs must be explicitly specified using an appropriate combination of firstPeriodStartDate, firstRegularPeriodStartDate and lastRegularPeriodEndDate."""
    effective_date: ForwardRef("AdjustableOrRelativeDate") = Field(None, description="The first day of the terms of the trade. This day may be subject to adjustment in accordance with a business day convention.")
    termination_date: ForwardRef("AdjustableOrRelativeDate") = Field(None, description="The last day of the terms of the trade. This date may be subject to adjustments in accordance with the business day convention. It can also be specified in relation to another scheduled date (e.g. the last payment date).")
    calculation_period_dates_adjustments: ForwardRef("BusinessDayAdjustments") = Field(None, description="The specification of the business day convention and financial business centers used for adjusting any calculation period date if it would otherwise fall on a day that is not a business day in the specified business center.")
    first_period_start_date: ForwardRef("AdjustableOrRelativeDate") = Field(None, description="The start date of the calculation period. FpML specifies that for interest rate swaps this date must only be specified if it is not equal to the effective date. It is always specified in the case of equity swaps and credit default swaps with periodic payments. This date may be subject to adjustment in accordance with a business day convention.")
    first_regular_period_start_date: str = Field(None, description="The start date of the regular part of the calculation period schedule. It must only be specified if there is an initial stub calculation period. This day may be subject to adjustment in accordance with any adjustments specified in calculationPeriodDatesAdjustments.")
    first_compounding_period_end_date: str = Field(None, description="The end date of the initial compounding period when compounding is applicable. It must only be specified when the compoundingMethod element is present and not equal to a value of None. This date may be subject to adjustment in accordance with any adjustments specified in calculationPeriodDatesAdjustments.")
    last_regular_period_end_date: str = Field(None, description="The end date of the regular part of the calculation period schedule. It must only be specified if there is a final stub calculation period. This day may be subject to adjustment in accordance with any adjustments specified in calculationPeriodDatesAdjustments.")
    stub_period_type: ForwardRef("StubPeriodTypeEnum") = Field(None, description="Method to allocate any irregular period remaining after regular periods have been allocated between the effective and termination date.")
    calculation_period_frequency: ForwardRef("CalculationPeriodFrequency") = Field(None, description="The frequency at which calculation period end dates occur with the regular part of the calculation period schedule and their roll date convention.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.adjustable_or_relative_date import AdjustableOrRelativeDate
from src.models.cdm.generated.base.datetime.business_day_adjustments import BusinessDayAdjustments
from src.models.cdm.generated.base.datetime.calculation_period_frequency import CalculationPeriodFrequency
from src.models.cdm.generated.product.common.schedule.stub_period_type_enum import StubPeriodTypeEnum
CalculationPeriodDates.model_rebuild()
