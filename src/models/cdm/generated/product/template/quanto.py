from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.business_center_time import BusinessCenterTime
    from src.models.cdm.generated.observable.asset.fx_rate import FxRate
    from src.models.cdm.generated.observable.asset.fx_spot_rate_source import FxSpotRateSource

class Quanto(CdmModelBase):
    """Determines the currency rate that the seller of the equity amounts will apply at each valuation date for converting the respective amounts into a currency that is different from the currency denomination of the underlier."""
    fx_rate: List[ForwardRef("FxRate")] = Field(None, description="Specifies a currency conversion rate.")
    fx_spot_rate_source: ForwardRef("FxSpotRateSource") = Field(None, description="Specifies the methodology (reference source and, optionally, fixing time) to be used for determining a currency conversion rate.")
    fixing_time: ForwardRef("BusinessCenterTime") = Field(None, description="The time at which the spot currency exchange rate will be observed. It is specified as a time in a business day calendar location, e.g. 11:00am London time.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.business_center_time import BusinessCenterTime
from src.models.cdm.generated.observable.asset.fx_rate import FxRate
from src.models.cdm.generated.observable.asset.fx_spot_rate_source import FxSpotRateSource
Quanto.model_rebuild()
