from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.business_centers import BusinessCenters
    from src.models.cdm.generated.base.datetime.business_day_convention_enum import BusinessDayConventionEnum

class BusinessDateRange(CdmModelBase):
    """A class defining a range of contiguous business days by defining an unadjusted first date, an unadjusted last date and a business day convention and business centers for adjusting the first and last dates if they would otherwise fall on a non business day in the specified business centers. The days between the first and last date must also be good business days in the specified centers to be counted in the range."""
    start_date: str = Field(None, description="The first date of a date range.")
    end_date: str = Field(None, description="The last date of a date range.")
    business_day_convention: ForwardRef("BusinessDayConventionEnum") = Field(description="The convention for adjusting a date if it would otherwise fall on a day that is not a business day, as specified by an ISDA convention (e.g. Following, Precedent).")
    business_centers: ForwardRef("BusinessCenters") = Field(None, description="The business center(s), specified either explicitly or by reference to those specified somewhere else in the instance document.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.business_centers import BusinessCenters
from src.models.cdm.generated.base.datetime.business_day_convention_enum import BusinessDayConventionEnum
BusinessDateRange.model_rebuild()
