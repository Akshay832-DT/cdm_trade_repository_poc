from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.math.quantity_change_direction_enum import QuantityChangeDirectionEnum
    from src.models.cdm.generated.base.staticdata.identifier.identifier import Identifier
    from src.models.cdm.generated.observable.asset.price_quantity import PriceQuantity

class QuantityChangeInstruction(CdmModelBase):
    """Instructions required to create a Quantity Change Primitive Event, which can be either an increase, a decrease or a replacement. An increase adds a new trade lot to the original trade, whereas a decrease subtracts from an existing trade lot's quantity. A replacement updates the quantity of an existing trade lot to the new value."""
    change: List[ForwardRef("PriceQuantity")] = Field(None, description="Quantity by which the trade is being increased, decreased or replaced, and the price at which such quantity change is agreed. The quantity change should always be specified as a positive number, with the direction (increase/decrease/replacement) being specified by the direction enumeration. A fee can also be associated to the quantity change by specifying a Price component of type CashPrice, including the corresponding settlement date and direction.")
    direction: ForwardRef("QuantityChangeDirectionEnum") = Field(description="Direction of the quantity change specified as either an increase, decrease or replacement.")
    lot_identifier: List[ForwardRef("Identifier")] = Field(None, description="Identifier for the new lot (in case of increase) or for the existing lot to be changed(in case of decrease or replacement). This optional attribute is mandatory in case of a decrease or replacement if the initial trade state contains multiple trade lots.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.math.quantity_change_direction_enum import QuantityChangeDirectionEnum
from src.models.cdm.generated.base.staticdata.identifier.identifier import Identifier
from src.models.cdm.generated.observable.asset.price_quantity import PriceQuantity
QuantityChangeInstruction.model_rebuild()
