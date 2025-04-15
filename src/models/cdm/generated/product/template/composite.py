from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.business_center_time import BusinessCenterTime
    from src.models.cdm.generated.base.datetime.relative_date_offset import RelativeDateOffset
    from src.models.cdm.generated.observable.asset.fx_spot_rate_source import FxSpotRateSource
    from src.models.cdm.generated.observable.common.determination_method_enum import DeterminationMethodEnum

class Composite(CdmModelBase):
    """Specifies the conditions to be applied for converting into a reference currency when the actual currency rate is not determined upfront."""
    determination_method: ForwardRef("DeterminationMethodEnum") = Field(None, description="Specifies the method according to which an amount or a date is determined.")
    relative_date: ForwardRef("RelativeDateOffset") = Field(None, description="A date specified as some offset to another date (the anchor date).")
    fx_spot_rate_source: ForwardRef("FxSpotRateSource") = Field(None, description="Specifies the methodology (reference source and, optionally, fixing time) to be used for determining a currency conversion rate.")
    fixing_time: ForwardRef("BusinessCenterTime") = Field(None, description="The time at which the spot currency exchange rate will be observed. It is specified as a time in a business day calendar location, e.g. 11:00am London time.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.business_center_time import BusinessCenterTime
from src.models.cdm.generated.base.datetime.relative_date_offset import RelativeDateOffset
from src.models.cdm.generated.observable.asset.fx_spot_rate_source import FxSpotRateSource
from src.models.cdm.generated.observable.common.determination_method_enum import DeterminationMethodEnum
Composite.model_rebuild()
