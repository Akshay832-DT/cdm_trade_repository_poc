from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.business_day_adjustments import BusinessDayAdjustments
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class AdjustableDates(CdmModelBase):
    """A class for defining a series of dates that shall be subject to adjustment if they would otherwise fall on a day that is not a business day in the specified business centers, together with the convention for adjusting the dates."""
    unadjusted_date: List[List] = Field(None, description="A date subject to adjustment.")
    date_adjustments: ForwardRef("BusinessDayAdjustments") = Field(None, description="The business day convention and financial business centers used for adjusting the date if it would otherwise fall on a day that is not a business date in the specified business centers.")
    adjusted_date: List[ForwardRef("FieldWithMetaString")] = Field(None, description="The date(s) once the adjustment has been performed. (Note that this date may change if the business center holidays change).")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.business_day_adjustments import BusinessDayAdjustments
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
AdjustableDates.model_rebuild()
