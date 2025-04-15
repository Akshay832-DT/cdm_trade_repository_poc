from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.template.schedule_period import SchedulePeriod

class CalculationSchedule(CdmModelBase):
    """A class that allows the full representation of a payout by defining a set of schedule periods. It supports standard schedule customization by expressing all the dates, quantities, and pricing data in a non-parametric way."""
    schedule_period: List[ForwardRef("SchedulePeriod")] = Field(None, description="Defines a period of a calculation schedule structure.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.template.schedule_period import SchedulePeriod
CalculationSchedule.model_rebuild()
