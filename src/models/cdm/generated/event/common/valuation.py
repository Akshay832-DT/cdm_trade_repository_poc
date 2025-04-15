from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.common.price_timing_enum import PriceTimingEnum
    from src.models.cdm.generated.event.common.valuation_source_enum import ValuationSourceEnum
    from src.models.cdm.generated.event.common.valuation_type_enum import ValuationTypeEnum
    from src.models.cdm.generated.observable.asset.money import Money
    from src.models.cdm.generated.observable.asset.price import Price

class Valuation(CdmModelBase):
    """Defines the value of an investment, asset, or security"""
    amount: ForwardRef("Money") = Field(description="Current value of the outstanding contract")
    timestamp: str = Field(description="Date and time of the last valuation marked to market, provided by the central counterparty (CCP) or calculated using the current or last available market price of the inputs.")
    method: ForwardRef("ValuationTypeEnum") = Field(None, description="Method used for the valuation of the transaction by the valuation party.")
    source: ForwardRef("ValuationSourceEnum") = Field(None, description="Source of the valuation of the transaction by the valuation party.")
    delta: float = Field(None, description="The ratio of the change in the price of a derivative transaction to the change in the price of the underlying. This field is applicable only to options and swaptions.")
    valuation_timing: ForwardRef("PriceTimingEnum") = Field(None, description="Denotes when the valuation was sourced during a business day.")
    price_component: ForwardRef("Price") = Field(None, description="Denotes the price used to compute the valuation.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.common.price_timing_enum import PriceTimingEnum
from src.models.cdm.generated.event.common.valuation_source_enum import ValuationSourceEnum
from src.models.cdm.generated.event.common.valuation_type_enum import ValuationTypeEnum
from src.models.cdm.generated.observable.asset.money import Money
from src.models.cdm.generated.observable.asset.price import Price
Valuation.model_rebuild()
