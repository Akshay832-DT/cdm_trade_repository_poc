from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CalculationPeriodData(CdmModelBase):
    """"""
    start_date: str = Field()
    end_date: str = Field()
    days_in_period: int = Field()
    days_in_leap_year_period: int = Field()
    is_first_period: bool = Field()
    is_last_period: bool = Field()

# Import after class definition to avoid circular imports
CalculationPeriodData.model_rebuild()
