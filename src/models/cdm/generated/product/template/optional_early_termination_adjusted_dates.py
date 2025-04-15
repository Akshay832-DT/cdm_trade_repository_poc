from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.template.early_termination_event import EarlyTerminationEvent

class OptionalEarlyTerminationAdjustedDates(CdmModelBase):
    """A data defining:  the adjusted dates associated with an optional early termination provision."""
    early_termination_event: List[ForwardRef("EarlyTerminationEvent")] = Field(None, description="The adjusted dates associated with an individual early termination date.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.template.early_termination_event import EarlyTerminationEvent
OptionalEarlyTerminationAdjustedDates.model_rebuild()
