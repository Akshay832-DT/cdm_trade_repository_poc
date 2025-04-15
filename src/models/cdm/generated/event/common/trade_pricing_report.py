from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.time_zone import TimeZone
    from src.models.cdm.generated.base.staticdata.asset.rates.floating_rate_index_enum import FloatingRateIndexEnum
    from src.models.cdm.generated.event.common.trade import Trade

class TradePricingReport(CdmModelBase):
    """The attributes that are specific for consensus based pricing reporting."""
    trade: ForwardRef("Trade") = Field(description="Represents the cosensus based pricing parameters on a trade basis.")
    pricing_time: ForwardRef("TimeZone") = Field(description="The regional exchange close time for the underlying contract,including time zone, at which the trades should be priced. This provides an indication for which regional snapshot should be used for pricing primarily for Global markets where there are multiple regional close times.")
    discounting_index: ForwardRef("FloatingRateIndexEnum") = Field(None, description="It specifies the interest payable on collateral delivered under a CSA covering the trade.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.time_zone import TimeZone
from src.models.cdm.generated.base.staticdata.asset.rates.floating_rate_index_enum import FloatingRateIndexEnum
from src.models.cdm.generated.event.common.trade import Trade
TradePricingReport.model_rebuild()
