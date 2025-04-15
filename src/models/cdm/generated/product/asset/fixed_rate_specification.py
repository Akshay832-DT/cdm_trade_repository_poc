from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.common.schedule.rate_schedule import RateSchedule

class FixedRateSpecification(CdmModelBase):
    """Type defining the specification for a fixed rate."""
    rate_schedule: ForwardRef("RateSchedule") = Field(None, description="The fixed rate or fixed rate schedule expressed as explicit fixed rates and dates. In the case of a schedule, the step dates may be subject to adjustment in accordance with any adjustments specified in calculationPeriodDatesAdjustments.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.common.schedule.rate_schedule import RateSchedule
FixedRateSpecification.model_rebuild()
