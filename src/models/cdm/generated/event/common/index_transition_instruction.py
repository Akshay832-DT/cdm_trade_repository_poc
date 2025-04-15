from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.common.transfer import Transfer
    from src.models.cdm.generated.observable.asset.price_quantity import PriceQuantity

class IndexTransitionInstruction(CdmModelBase):
    """Defines the information needed to create a Index Transition Business Event."""
    price_quantity: List[ForwardRef("PriceQuantity")] = Field(None, description="Specifies both new floating rate index and spread adjustment for each leg to be updated.  The spread adjustment accounts for the difference between the old floating rate index relative to the new one. This spread amount is added to the existing spread to determine the new spread, which is applied from the specified effective date forward. In the case of the IBOR Fallback Rate Adjustments, the adjustment spread (also known as the Fallback Adjustment) accounts for two distinctions: i) the fact that the replacement Risk-Free Rate is an overnight rate while IBORs have term structures (e.g., 1, 3, 6-month LIBOR); and (ii) the historical spread differential between IBORs and their term equivalent Overnight Risk-Free Rate compounded rates.")
    effective_date: str = Field(description="Specifies the effective date of the index transition event. This is first date on which the floating rate calculation will use the new floating rate index and adjusted spread in the floating rate calculation.")
    cash_transfer: ForwardRef("Transfer") = Field(None, description="Specifies the cash transfer that can optionally be tied to an index transition event.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.common.transfer import Transfer
from src.models.cdm.generated.observable.asset.price_quantity import PriceQuantity
IndexTransitionInstruction.model_rebuild()
