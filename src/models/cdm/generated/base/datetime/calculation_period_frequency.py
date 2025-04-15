from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.period_extended_enum import PeriodExtendedEnum
    from src.models.cdm.generated.base.datetime.roll_convention_enum import RollConventionEnum

class CalculationPeriodFrequency(CdmModelBase):
    """A class to specify the frequency at which calculation period end dates occur within the regular part of the calculation period schedule and their roll date convention."""
    period_multiplier: int = Field(None, description="A time period multiplier, e.g. 1, 2, or 3. If the period value is T (Term) then period multiplier must contain the value 1.")
    period: ForwardRef("PeriodExtendedEnum") = Field(None, description="A time period, e.g. a day, week, month, year or term of the stream.")
    roll_convention: ForwardRef("RollConventionEnum") = Field(description="The roll convention specifies the period term as part of a periodic schedule, i.e. the calculation period end date within the regular part of the calculation period. The value could be a rule, e.g. IMM Settlement Dates, which is the 3rd Wednesday of the month, or it could be a specific day of the month, such as the first day of the applicable month. It is used in conjunction with a frequency and the regular period start date of a calculation period.")
    balance_of_first_period: bool = Field(None, description="Indicates, when true, that that the first Calculation Period should run from the Effective Date to the end of the calendar period in which the Effective Date falls, e.g. Jan 15 - Jan 31 if the calculation periods are one month long and Effective Date is Jan 15. If false, the first Calculation Period should run from the Effective Date for one whole period, e.g. Jan 15 to Feb 14 if the calculation periods are one month long and Effective Date is Jan 15. Mostly used in Commmodity Swaps.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.period_extended_enum import PeriodExtendedEnum
from src.models.cdm.generated.base.datetime.roll_convention_enum import RollConventionEnum
CalculationPeriodFrequency.model_rebuild()
