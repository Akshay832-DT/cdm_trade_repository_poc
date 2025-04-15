from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.template.cancellation_event import CancellationEvent

class CancelableProvisionAdjustedDates(CdmModelBase):
    """A data to:  define the adjusted dates for a cancelable provision on a swap transaction."""
    cancellation_event: List[ForwardRef("CancellationEvent")] = Field(None, description="The adjusted dates for an individual cancellation date.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.template.cancellation_event import CancellationEvent
CancelableProvisionAdjustedDates.model_rebuild()
