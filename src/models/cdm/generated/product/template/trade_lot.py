from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.identifier.identifier import Identifier
    from src.models.cdm.generated.observable.asset.price_quantity import PriceQuantity

class TradeLot(CdmModelBase):
    """Specifies the price and quantity of a trade lot, where the same product could be traded multiple times with the same counterparty but in different lots (at a different date, in a different quantity and at a different price). One trade lot combined with a product definition specifies the entire economics of a trade. The lifecycle mechanics of each such trade lot (e.g. cashflow payments) is independent of the other lots."""
    lot_identifier: List[ForwardRef("Identifier")] = Field(None, description="Specifies one or more identifiers for the lot, if any.")
    price_quantity: List[ForwardRef("PriceQuantity")] = Field(None, description="Specifies the settlement characteristics of a trade lot: price, quantity, observable (optionally) and the settlement terms. This attribute has a multiple cardinality to allow to specify the price, quantity and observable of different legs in a single, composite product (e.g. a Swap).")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.identifier.identifier import Identifier
from src.models.cdm.generated.observable.asset.price_quantity import PriceQuantity
TradeLot.model_rebuild()
