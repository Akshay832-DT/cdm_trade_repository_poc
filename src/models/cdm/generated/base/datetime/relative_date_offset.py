from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.business_centers import BusinessCenters
    from src.models.cdm.generated.base.datetime.business_day_convention_enum import BusinessDayConventionEnum
    from src.models.cdm.generated.base.datetime.day_type_enum import DayTypeEnum
    from src.models.cdm.generated.base.datetime.period_enum import PeriodEnum
    from src.models.cdm.generated.metafields.reference_with_meta_business_centers import ReferenceWithMetaBusinessCenters
    from src.models.cdm.generated.metafields.reference_with_meta_string import ReferenceWithMetaString

class RelativeDateOffset(CdmModelBase):
    """A class defining a date (referred to as the derived date) as a relative offset from another date (referred to as the anchor date). If the anchor date is itself an adjustable date then the offset is assumed to be calculated from the adjusted anchor date. A number of different scenarios can be supported, namely; 1) the derived date may simply be a number of calendar periods (days, weeks, months or years) preceding or following the anchor date; 2) the unadjusted derived date may be a number of calendar periods (days, weeks, months or years) preceding or following the anchor date with the resulting unadjusted derived date subject to adjustment in accordance with a specified business day convention, i.e. the derived date must fall on a good business day; 3) the derived date may be a number of business days preceding or following the anchor date. Note that the businessDayConvention specifies any required adjustment to the unadjusted derived date. A negative or positive value in the periodMultiplier indicates whether the unadjusted derived precedes or follows the anchor date. The businessDayConvention should contain a value NONE if the day type element contains a value of Business (since specifying a negative or positive business days offset would already guarantee that the derived date would fall on a good business day in the specified business centers)."""
    period_multiplier: int = Field(None, description="A time period multiplier, e.g. 1, 2 or 3 etc. A negative value can be used when specifying an offset relative to another date, e.g. -2 days.")
    period: ForwardRef("PeriodEnum") = Field(None, description="A time period, e.g. a day, week, month or year of the stream. If the periodMultiplier value is 0 (zero) then period must contain the value D (day).")
    day_type: ForwardRef("DayTypeEnum") = Field(None, description="In the case of an offset specified as a number of days, this element defines whether consideration is given as to whether a day is a good business day or not. If a day type of business days is specified then non-business days are ignored when calculating the offset. The financial business centers to use for determination of business days are implied by the context in which this element is used. This element must only be included when the offset is specified as a number of days. If the offset is zero days then the dayType element should not be included.")
    business_day_convention: ForwardRef("BusinessDayConventionEnum") = Field(description="The convention for adjusting a date if it would otherwise fall on a day that is not a business day, as specified by an ISDA convention (e.g. Following, Precedent).")
    business_centers: ForwardRef("BusinessCenters") = Field(None)
    business_centers_reference: ForwardRef("ReferenceWithMetaBusinessCenters") = Field(None, description="A pointer style reference to a set of financial business centers defined elsewhere in the document. This set of business centers is used to determine whether a particular day is a business day or not.")
    date_relative_to: ForwardRef("ReferenceWithMetaString") = Field(None, description="Specifies the anchor as an href attribute. The href attribute value is a pointer style reference to the element or component elsewhere in the document where the anchor date is defined.")
    adjusted_date: str = Field(None, description="The date once the adjustment has been performed. (Note that this date may change if the business center holidays change).")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.business_centers import BusinessCenters
from src.models.cdm.generated.base.datetime.business_day_convention_enum import BusinessDayConventionEnum
from src.models.cdm.generated.base.datetime.day_type_enum import DayTypeEnum
from src.models.cdm.generated.base.datetime.period_enum import PeriodEnum
from src.models.cdm.generated.metafields.reference_with_meta_business_centers import ReferenceWithMetaBusinessCenters
from src.models.cdm.generated.metafields.reference_with_meta_string import ReferenceWithMetaString
RelativeDateOffset.model_rebuild()
