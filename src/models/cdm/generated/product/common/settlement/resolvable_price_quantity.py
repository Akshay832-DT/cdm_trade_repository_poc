from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.math.quantity import Quantity
    from src.models.cdm.generated.metafields.reference_with_meta_non_negative_quantity_schedule import ReferenceWithMetaNonNegativeQuantitySchedule
    from src.models.cdm.generated.metafields.reference_with_meta_price_schedule import ReferenceWithMetaPriceSchedule
    from src.models.cdm.generated.metafields.reference_with_meta_resolvable_price_quantity import ReferenceWithMetaResolvablePriceQuantity
    from src.models.cdm.generated.product.asset.future_value_amount import FutureValueAmount
    from src.models.cdm.generated.product.common.settlement.quantity_multiplier import QuantityMultiplier

class ResolvablePriceQuantity(CdmModelBase):
    """Generic class to specify the quantity for different payout legs in a contractual product, when that quantity can vary across payout legs or across time. A resolvable quantity can always be resolved into a single quantity from the quantity notation which has a corresponding asset identifier. In addition to the base case, where quantity is directly specified as a number as part of the quantity notation, the other use cases are: (i) quantity based on some pre-defined schedule (eg amortising notional), (ii) quantity based on some pre-defined events (eg resetting cross-currency notional), or quantity set as reference to another quantity (eg equity notional as no. securities x price)."""
    resolved_quantity: ForwardRef("Quantity") = Field(None, description="A product's quantity as a single, non-negative amount.  When specified as part of a product definition, this quantity attribute would not be set.  Instead it is specified on the quantity notation along with an asset identifier matching this payout's asset identifier.  This allows the quantity to be resolved for a payout leg, which can then be specified here for convenience during data processing.  There needs to be at least one resolvable quantity across payout legs of a product to define an anchor that other payout quantities can refer to.  This attribute is ignored when mapping existing FpML messages.")
    quantity_schedule: ForwardRef("ReferenceWithMetaNonNegativeQuantitySchedule") = Field(None, description="A payout's quantity specified as a schedule, which may also contain a single value if that quantity is constant. There can only be a single quantity schedule applicable to a payout: e.g. the notional for an interest rate leg. The quantity must be specified outside of the payout in a PriceQuantity object and only referenced inside the payout using an address.")
    quantity_reference: ForwardRef("ReferenceWithMetaResolvablePriceQuantity") = Field(None, description="Reference quantity when resolvable quantity is defined as relative to another (resolvable) quantity. A resolvable quantity needs to contain either an absolute quantity or a reference to another (resolvable) quantity. This requirement is captured by a choice rule on the class.")
    quantity_multiplier: ForwardRef("QuantityMultiplier") = Field(None, description="Quantity multiplier is specified on top of a reference quantity and is used as a multiplying factor when resolving the quantity. A quantity multiplier can only exist when the resolvable quantity specifies a reference quantity.")
    reset: bool = Field(None, description="Whether the quantity is resettable")
    future_value_notional: ForwardRef("FutureValueAmount") = Field(None, description="The future value notional is specific to BRL CDI swaps, and is specified alongside the notional amount. The value is calculated as follows: Future Value Notional = Notional Amount * (1 + Fixed Rate) ^ (Fixed Rate Day Count Fraction). The currency should always match that expressed in the notional schedule. The value date should match the adjusted termination date.")
    price_schedule: List[ForwardRef("ReferenceWithMetaPriceSchedule")] = Field(None, description="A payout's price specified as a schedule, which may also contain a single value if that price is constant. There may be multiple prices specified for a single payout: e.g. a floating interest rate leg may specify a spread, a cap and/or floor and a multiplier. The price must be specified outside of the payout in a PriceQuantity object and only referenced inside the payout using an address.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.math.quantity import Quantity
from src.models.cdm.generated.metafields.reference_with_meta_non_negative_quantity_schedule import ReferenceWithMetaNonNegativeQuantitySchedule
from src.models.cdm.generated.metafields.reference_with_meta_price_schedule import ReferenceWithMetaPriceSchedule
from src.models.cdm.generated.metafields.reference_with_meta_resolvable_price_quantity import ReferenceWithMetaResolvablePriceQuantity
from src.models.cdm.generated.product.asset.future_value_amount import FutureValueAmount
from src.models.cdm.generated.product.common.settlement.quantity_multiplier import QuantityMultiplier
ResolvablePriceQuantity.model_rebuild()
