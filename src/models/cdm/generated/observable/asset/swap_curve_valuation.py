from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.period import Period
    from src.models.cdm.generated.base.staticdata.asset.rates.floating_rate_index_enum import FloatingRateIndexEnum
    from src.models.cdm.generated.observable.asset.quotation_side_enum import QuotationSideEnum

class SwapCurveValuation(CdmModelBase):
    """A class to specify a valuation swap curve, which is used as part of the strike construct for the bond and convertible bond options."""
    floating_rate_index: ForwardRef("FloatingRateIndexEnum") = Field()
    index_tenor: ForwardRef("Period") = Field(None, description="The ISDA Designated Maturity, i.e. the tenor of the floating rate.")
    spread: float = Field(description="Spread in basis points over the floating rate index.")
    side: ForwardRef("QuotationSideEnum") = Field(None, description="The side (bid/mid/ask) of the measure.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.period import Period
from src.models.cdm.generated.base.staticdata.asset.rates.floating_rate_index_enum import FloatingRateIndexEnum
from src.models.cdm.generated.observable.asset.quotation_side_enum import QuotationSideEnum
SwapCurveValuation.model_rebuild()
