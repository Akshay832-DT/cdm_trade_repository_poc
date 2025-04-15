from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_business_center_enum import FieldWithMetaBusinessCenterEnum

class BusinessCenterTime(CdmModelBase):
    """A class for defining a time with respect to a business day calendar location. For example, 11:00:00 GBLO."""
    hour_minute_time: str = Field(description="A time specified in hh:mm:ss format where the second component must be '00', e.g. 11am would be represented as 11:00:00.")
    business_center: ForwardRef("FieldWithMetaBusinessCenterEnum") = Field(description="A code identifying a business day calendar location. A business day calendar location is drawn from the list identified by the business day calendar location enumeration.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_business_center_enum import FieldWithMetaBusinessCenterEnum
BusinessCenterTime.model_rebuild()
