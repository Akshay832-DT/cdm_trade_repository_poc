from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.math.quantity import Quantity
    from src.models.cdm.generated.base.staticdata.party.payer_receiver import PayerReceiver
    from src.models.cdm.generated.event.common.reset import Reset
    from src.models.cdm.generated.event.common.trade_state import TradeState
    from src.models.cdm.generated.metafields.reference_with_meta_payout import ReferenceWithMetaPayout

class CalculateTransferInstruction(CdmModelBase):
    """Defines the tradeState or payout on which to create a Transfer along with all necessary resets."""
    trade_state: ForwardRef("TradeState") = Field()
    payout: ForwardRef("ReferenceWithMetaPayout") = Field()
    resets: List[ForwardRef("Reset")] = Field(None)
    payer_receiver: ForwardRef("PayerReceiver") = Field(None)
    quantity: ForwardRef("Quantity") = Field(None, description="Specifies quantity amount returned if not the full amount from the TradeState, e.g. partial return")
    date: str = Field(None)

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.math.quantity import Quantity
from src.models.cdm.generated.base.staticdata.party.payer_receiver import PayerReceiver
from src.models.cdm.generated.event.common.reset import Reset
from src.models.cdm.generated.event.common.trade_state import TradeState
from src.models.cdm.generated.metafields.reference_with_meta_payout import ReferenceWithMetaPayout
CalculateTransferInstruction.model_rebuild()
