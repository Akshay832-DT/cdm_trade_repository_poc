from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.event.trigger_event import TriggerEvent

class Barrier(CdmModelBase):
    """As per ISDA 2002 Definitions."""
    barrier_cap: ForwardRef("TriggerEvent") = Field(None, description="A trigger level approached from beneath.")
    barrier_floor: ForwardRef("TriggerEvent") = Field(None, description="A trigger level approached from above.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.event.trigger_event import TriggerEvent
Barrier.model_rebuild()
