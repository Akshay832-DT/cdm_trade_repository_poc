from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_settlement_rate_option_enum import FieldWithMetaSettlementRateOptionEnum
    from src.models.cdm.generated.observable.asset.price_source_disruption import PriceSourceDisruption

class SettlementRateOption(CdmModelBase):
    """Defines the settlement rate option to use for fixing in case of cash settlement. Currently only applicable to foreign exchange fixing in case of cross-currency settlement."""
    settlement_rate_option: ForwardRef("FieldWithMetaSettlementRateOptionEnum") = Field(description="The rate source for the conversion to the settlement currency. This source is specified through a scheme that reflects the terms of the Annex A to the 1998 FX and Currency Option Definitions.")
    price_source_disruption: ForwardRef("PriceSourceDisruption") = Field(None, description="An attribute defining the parameters to get a new quote when a settlement rate option is disrupted.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_settlement_rate_option_enum import FieldWithMetaSettlementRateOptionEnum
from src.models.cdm.generated.observable.asset.price_source_disruption import PriceSourceDisruption
SettlementRateOption.model_rebuild()
