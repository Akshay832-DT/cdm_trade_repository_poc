from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.period_time_enum import PeriodTimeEnum

class Velocity(CdmModelBase):
    """"""
    period_multiplier: int = Field(None)
    period: ForwardRef("PeriodTimeEnum") = Field(None)

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.period_time_enum import PeriodTimeEnum
Velocity.model_rebuild()
