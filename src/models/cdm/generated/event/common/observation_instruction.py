from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.common.observation_event import ObservationEvent

class ObservationInstruction(CdmModelBase):
    """Specifies inputs needed to process an observation."""
    observation_event: ForwardRef("ObservationEvent") = Field(description="Contains all information related to an observation.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.common.observation_event import ObservationEvent
ObservationInstruction.model_rebuild()
