from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.fro.business_day_offset import BusinessDayOffset
    from src.models.cdm.generated.observable.asset.fro.floating_rate_index_fixing_time import FloatingRateIndexFixingTime

class FloatingRateIndexFixingDetails(CdmModelBase):
    """This type holds parameters defining the fixingt time and offset for a floating rate index."""
    fixing_time: ForwardRef("FloatingRateIndexFixingTime") = Field(None, description="Parameters defining the normal fixing time (can vary by index tenor / designated maturity).")
    fixing_offset: ForwardRef("BusinessDayOffset") = Field(None, description="Parameters defining the normal fixing offset (can vary by index tenor / designated maturity).")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.fro.business_day_offset import BusinessDayOffset
from src.models.cdm.generated.observable.asset.fro.floating_rate_index_fixing_time import FloatingRateIndexFixingTime
FloatingRateIndexFixingDetails.model_rebuild()
