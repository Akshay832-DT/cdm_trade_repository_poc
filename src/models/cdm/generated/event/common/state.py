from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.common.closed_state import ClosedState
    from src.models.cdm.generated.event.position.position_status_enum import PositionStatusEnum

class State(CdmModelBase):
    """Defines the state of a trade at a point in the Trade's life cycle. Trades have many state dimensions, all of which are represented here. For example, states useful for position keeping are represented alongside those needed for regulatory reporting."""
    closed_state: ForwardRef("ClosedState") = Field(None, description="Represents the qualification of what led to the trade's closure alongside the dates on which this closure took effect.")
    position_state: ForwardRef("PositionStatusEnum") = Field(None, description="Identifies the state of the position, to distinguish if just executed, formed, already settled, closed, etc.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.common.closed_state import ClosedState
from src.models.cdm.generated.event.position.position_status_enum import PositionStatusEnum
State.model_rebuild()
