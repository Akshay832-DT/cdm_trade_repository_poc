from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class TimeZone(CdmModelBase):
    """The time alongside with the timezone location information. This class makes use of the FpML TimezoneLocation construct."""
    time: str = Field(description="The observation time.")
    location: ForwardRef("FieldWithMetaString") = Field(None, description="FpML specifies the timezoneLocationScheme by reference to the Time Zone Database (a.k.a. tz database) maintained by IANA, the Internet Assigned Numbers Authority.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
TimeZone.model_rebuild()
