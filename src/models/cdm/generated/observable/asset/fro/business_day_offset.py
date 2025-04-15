from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.business_centers import BusinessCenters
    from src.models.cdm.generated.base.datetime.period_enum import PeriodEnum

class BusinessDayOffset(CdmModelBase):
    """This allows an offset to be specified as, for instance, N business days, with a business centers specified as included."""
    period_multiplier: int = Field(None, description="A time period multiplier, e.g. 1, 2 or 3 etc. A negative value can be used when specifying an offset relative to another date, e.g. -2 days.")
    period: ForwardRef("PeriodEnum") = Field(None, description="A time period, e.g. a day, week, month or year of the stream. If the periodMultiplier value is 0 (zero) then period must contain the value D (day).")
    business_centers: ForwardRef("BusinessCenters") = Field(None, description="The business centers for the offset.")
    fixing_offset_definition: str = Field(None, description="Legal text that underlies the Fixing Offset. ISDA Fixing Offset Definition. (e.g. One day that is either a Sydney Business Day or a Melbourne Business Day following the Reset Date)")
    fixing_offset_reason: str = Field(None, description="Fixing Offset Reason")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.business_centers import BusinessCenters
from src.models.cdm.generated.base.datetime.period_enum import PeriodEnum
BusinessDayOffset.model_rebuild()
