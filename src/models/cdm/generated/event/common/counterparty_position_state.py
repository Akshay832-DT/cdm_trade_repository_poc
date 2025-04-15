from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.common.observation_event import ObservationEvent
    from src.models.cdm.generated.event.common.state import State
    from src.models.cdm.generated.event.common.valuation import Valuation
    from src.models.cdm.generated.event.position.counterparty_position import CounterpartyPosition

class CounterpartyPositionState(CdmModelBase):
    """Defines the fundamental financial information that can be changed by a Primitive Event and by extension any business or life-cycle event. Each PositionState specifies where a Position is in its life-cycle. PositionState is a root type and as such, can be created independently to any other CDM data type, but can also be used as part of the CDM Event Model."""
    counterparty_position: ForwardRef("CounterpartyPosition") = Field(description="Represents the Position that has been effected by a business or life-cycle event.")
    state: ForwardRef("State") = Field(None, description="Represents the State of the Position through its life-cycle.")
    observation_history: List[ForwardRef("ObservationEvent")] = Field(None, description="Represents the observed events related to a particular product or process, such as credit events or corporate actions.")
    valuation_history: List[ForwardRef("Valuation")] = Field(None)

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.common.observation_event import ObservationEvent
from src.models.cdm.generated.event.common.state import State
from src.models.cdm.generated.event.common.valuation import Valuation
from src.models.cdm.generated.event.position.counterparty_position import CounterpartyPosition
CounterpartyPositionState.model_rebuild()
