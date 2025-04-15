from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.period_extended_enum import PeriodExtendedEnum
    from src.models.cdm.generated.product.common.schedule.weekly_roll_convention_enum import WeeklyRollConventionEnum

class ResetFrequency(CdmModelBase):
    """A class defining the reset frequency. In the case of a weekly reset, also specifies the day of the week that the reset occurs. If the reset frequency is greater than the calculation period frequency the this implies that more or more reset dates is established for each calculation period and some form of rate averaging is applicable. The specific averaging method of calculation is specified in FloatingRateCalculation. In case the reset frequency is of value T (term), the period is defined by the swap/swapStream/calculationPerioDates/effectiveDate and the swap/swapStream/calculationPerioDates/terminationDate."""
    period_multiplier: int = Field(None, description="A time period multiplier, e.g. 1, 2, or 3. If the period value is T (Term) then period multiplier must contain the value 1.")
    period: ForwardRef("PeriodExtendedEnum") = Field(None, description="A time period, e.g. a day, week, month, year or term of the stream.")
    weekly_roll_convention: ForwardRef("WeeklyRollConventionEnum") = Field(None, description="The day of the week on which a weekly reset date occurs. This element must be included if the reset frequency is defined as weekly and not otherwise.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.period_extended_enum import PeriodExtendedEnum
from src.models.cdm.generated.product.common.schedule.weekly_roll_convention_enum import WeeklyRollConventionEnum
ResetFrequency.model_rebuild()
