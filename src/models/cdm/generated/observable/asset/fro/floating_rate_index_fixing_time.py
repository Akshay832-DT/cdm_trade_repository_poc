from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_business_center_enum import FieldWithMetaBusinessCenterEnum

class FloatingRateIndexFixingTime(CdmModelBase):
    """This type holds parameters defining the normal fixing time for a floating rate index."""
    hour_minute_time: str = Field(None, description="A time specified in hh:mm:ss format where the second component must be '00', e.g. 11am would be represented as 11:00:00.")
    business_center: ForwardRef("FieldWithMetaBusinessCenterEnum") = Field(None, description="A code identifying a business day calendar location. A business day calendar location is drawn from the list identified by the business day calendar location enumeration.")
    designated_maturity: str = Field(None, description="Allows a designed maturity to be specified for the fixing time.")
    fixing_time_definition: str = Field(None, description="Legal text that underlies the Fixing Time. ISDA Fixing Time Definition. (e.g. 09:30, Sydney time).")
    fixing_reason: str = Field(None, description="Fixing Reason")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_business_center_enum import FieldWithMetaBusinessCenterEnum
FloatingRateIndexFixingTime.model_rebuild()
