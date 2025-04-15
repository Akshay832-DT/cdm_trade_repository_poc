from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.ancillary_party import AncillaryParty
    from src.models.cdm.generated.base.staticdata.party.counterparty import Counterparty
    from src.models.cdm.generated.product.common.notional_adjustment_enum import NotionalAdjustmentEnum
    from src.models.cdm.generated.product.template.non_transferable_product import NonTransferableProduct
    from src.models.cdm.generated.product.template.trade_lot import TradeLot

class TradableProduct(CdmModelBase):
    """Definition of a product as ready to be traded, i.e. included in an execution or contract, by associating a specific price and quantity to this product plus an (optional) mechanism for any potential future quantity adjustment."""
    product: ForwardRef("NonTransferableProduct") = Field(description="The underlying product to be included in a contract or execution.")
    trade_lot: List[ForwardRef("TradeLot")] = Field(None, description="Specifies the price, quantity and effective date of each trade lot, when the same product may be traded multiple times in different lots with the same counterparty. In a trade increase, a new trade lot is added to the list, with the corresponding effective date. In a trade decrease, the existing trade lot(s) are decreased of the corresponding quantity (and an unwind fee may have to be settled). The multiple cardinality and the ability to increase existing trades is used for Equity Swaps in particular.")
    counterparty: List[ForwardRef("Counterparty")] = Field(None, description="Specifies the parties which are the two counterparties to the transaction.  The product is agnostic to the actual parties to the transaction, with the party references abstracted away from the product definition and replaced by the counterparty enum (e.g. CounterpartyEnum values Party1 or Party2). The counterparty enum can then be positioned in the product (e.g. to specify which counterparty is the payer, receiver etc) and this counterparties attribute, which is positioned outside of the product definition, allows the counterparty enum to be associated with an actual party reference.")
    ancillary_party: List[ForwardRef("AncillaryParty")] = Field(None, description="Specifies the parties with ancillary roles in the transaction. The product is agnostic to the actual parties involved in the transaction, with the party references abstracted away from the product definition and replaced by the AncillaryRoleEnum. The AncillaryRoleEnum can then be positioned in the product and this AncillaryParty type, which is positioned outside of the product definition, allows the AncillaryRoleEnum to be associated with an actual party reference.")
    adjustment: ForwardRef("NotionalAdjustmentEnum") = Field(None, description="Specifies the conditions that govern the adjustment to the quantity of a product being traded: e.g. execution, portfolio rebalancing etc. It is typically used in the context of Equity Swaps.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.ancillary_party import AncillaryParty
from src.models.cdm.generated.base.staticdata.party.counterparty import Counterparty
from src.models.cdm.generated.product.common.notional_adjustment_enum import NotionalAdjustmentEnum
from src.models.cdm.generated.product.template.non_transferable_product import NonTransferableProduct
from src.models.cdm.generated.product.template.trade_lot import TradeLot
TradableProduct.model_rebuild()
