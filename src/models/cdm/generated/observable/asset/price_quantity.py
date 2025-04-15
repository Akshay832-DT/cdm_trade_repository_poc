from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.adjustable_or_relative_date import AdjustableOrRelativeDate
    from src.models.cdm.generated.metafields.field_with_meta_non_negative_quantity_schedule import FieldWithMetaNonNegativeQuantitySchedule
    from src.models.cdm.generated.metafields.field_with_meta_observable import FieldWithMetaObservable
    from src.models.cdm.generated.metafields.field_with_meta_price_schedule import FieldWithMetaPriceSchedule

class PriceQuantity(CdmModelBase):
    """Defines a settlement as an exchange between two parties of a specified quantity of an asset (the quantity) against a specified quantity of another asset (the price). The settlement is optional and can be either cash or physical. The quantity can additionally be specified in terms of one or more currency amounts. In the case of non-cash products, the settlement of the price/quantity would not be specified here and instead would be delegated to the product mechanics, as parameterised by the price/quantity values."""
    price: List[ForwardRef("FieldWithMetaPriceSchedule")] = Field(None, description="Specifies a price to be used for trade amounts and other purposes.")
    quantity: List[ForwardRef("FieldWithMetaNonNegativeQuantitySchedule")] = Field(None, description="Specifies a quantity to be associated with an event, for example a trade amount.")
    observable: ForwardRef("FieldWithMetaObservable") = Field(None, description="Specifies the object to be observed for a price, it could be an asset or an index. The cardinality is optional as some quantity / price cases have no observable (e.g. a fixed rate in a given currency).")
    effective_date: ForwardRef("AdjustableOrRelativeDate") = Field(None, description="Specifies the date at which the price and quantity become effective. This day may be subject to adjustment in accordance with a business day convention, or could be specified as relative to a trade date, for instance. Optional cardinality, as the effective date is usually specified in the product definition, so it may only need to be specified as part of the PriceQuantity in an increase/decrease scenario for an existing trade.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.adjustable_or_relative_date import AdjustableOrRelativeDate
from src.models.cdm.generated.metafields.field_with_meta_non_negative_quantity_schedule import FieldWithMetaNonNegativeQuantitySchedule
from src.models.cdm.generated.metafields.field_with_meta_observable import FieldWithMetaObservable
from src.models.cdm.generated.metafields.field_with_meta_price_schedule import FieldWithMetaPriceSchedule
PriceQuantity.model_rebuild()
