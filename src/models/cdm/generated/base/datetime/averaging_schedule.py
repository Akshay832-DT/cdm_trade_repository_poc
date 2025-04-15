from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.calculation_period_frequency import CalculationPeriodFrequency

class AveragingSchedule(CdmModelBase):
    """Class to representing a method for generating a series of dates."""
    start_date: str = Field(description="Date on which this period begins.")
    end_date: str = Field(description="Date on which this period ends.")
    averaging_period_frequency: ForwardRef("CalculationPeriodFrequency") = Field(description="The frequency at which averaging period occurs with the regular part of the valuation schedule and their roll date convention.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.calculation_period_frequency import CalculationPeriodFrequency
AveragingSchedule.model_rebuild()
