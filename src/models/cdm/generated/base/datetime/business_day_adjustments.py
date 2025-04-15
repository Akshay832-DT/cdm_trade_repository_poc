from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.business_centers import BusinessCenters
    from src.models.cdm.generated.base.datetime.business_day_convention_enum import BusinessDayConventionEnum

class BusinessDayAdjustments(CdmModelBase):
    """A class defining the business day convention and financial business centers used for adjusting any relevant date if it would otherwise fall on a day that is not a business day in the specified business center."""
    business_day_convention: ForwardRef("BusinessDayConventionEnum") = Field(description="The convention for adjusting a date if it would otherwise fall on a day that is not a business day.")
    business_centers: ForwardRef("BusinessCenters") = Field(None, description="The business center(s), specified either explicitly or by reference to those specified somewhere else in the instance document.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.business_centers import BusinessCenters
from src.models.cdm.generated.base.datetime.business_day_convention_enum import BusinessDayConventionEnum
BusinessDayAdjustments.model_rebuild()
