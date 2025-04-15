from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.event.trigger_event import TriggerEvent

class Knock(CdmModelBase):
    """Knock In means option to exercise comes into existence. Knock Out means option to exercise goes out of existence."""
    knock_in: ForwardRef("TriggerEvent") = Field(None, description="The knock in.")
    knock_out: ForwardRef("TriggerEvent") = Field(None, description="The knock out.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.event.trigger_event import TriggerEvent
Knock.model_rebuild()
