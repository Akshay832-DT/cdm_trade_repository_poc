from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.common.observation_event import ObservationEvent
    from src.models.cdm.generated.event.common.reset import Reset
    from src.models.cdm.generated.event.common.state import State
    from src.models.cdm.generated.event.common.trade import Trade
    from src.models.cdm.generated.event.common.transfer_state import TransferState
    from src.models.cdm.generated.event.common.valuation import Valuation

class TradeState(CdmModelBase):
    """Defines the fundamental financial information that can be changed by a Primitive Event and by extension any business or life-cycle event. Each TradeState specifies where a Trade is in its life-cycle. TradeState is a root type and as such, can be created independently to any other CDM data type, but can also be used as part of the CDM Event Model."""
    trade: ForwardRef("Trade") = Field(description="Represents the Trade that has been effected by a business or life-cycle event.")
    state: ForwardRef("State") = Field(None, description="Represents the State of the Trade through its life-cycle.")
    reset_history: List[ForwardRef("Reset")] = Field(None, description="Represents the updated Trade attributes which can change as the result of a reset event. Only the changed values are captured, leaving the remaining data attributes empty. See Create_Reset function for further details on how TradeState is used in the Reset event. The TradeState data type is used to maintain backwards compatibility with the current Reset mechanism.")
    transfer_history: List[ForwardRef("TransferState")] = Field(None, description="Represents the updated Trade attributes which can change as the result of a transfer event.")
    observation_history: List[ForwardRef("ObservationEvent")] = Field(None, description="Represents the observed events related to a particular product or process, such as credit events or corporate actions.")
    valuation_history: List[ForwardRef("Valuation")] = Field(None)

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.common.observation_event import ObservationEvent
from src.models.cdm.generated.event.common.reset import Reset
from src.models.cdm.generated.event.common.state import State
from src.models.cdm.generated.event.common.trade import Trade
from src.models.cdm.generated.event.common.transfer_state import TransferState
from src.models.cdm.generated.event.common.valuation import Valuation
TradeState.model_rebuild()
