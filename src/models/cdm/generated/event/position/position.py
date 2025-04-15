from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.reference_with_meta_trade_state import ReferenceWithMetaTradeState
    from src.models.cdm.generated.observable.asset.money import Money
    from src.models.cdm.generated.observable.asset.price_quantity import PriceQuantity
    from src.models.cdm.generated.product.template.product import Product

class Position(CdmModelBase):
    """A Position describes how much of a given Product is being held and constitutes the atomic element of a Portfolio."""
    price_quantity: List[ForwardRef("PriceQuantity")] = Field(None, description="Position with many price quantities.")
    product: ForwardRef("Product") = Field(description="The product underlying the position.")
    cash_balance: ForwardRef("Money") = Field(None, description="The aggregate cost of proceeds")
    trade_reference: ForwardRef("ReferenceWithMetaTradeState") = Field(None, description="Reference to the Contract, in case product is contractual and the contract has been formed")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.reference_with_meta_trade_state import ReferenceWithMetaTradeState
from src.models.cdm.generated.observable.asset.money import Money
from src.models.cdm.generated.observable.asset.price_quantity import PriceQuantity
from src.models.cdm.generated.product.template.product import Product
Position.model_rebuild()
