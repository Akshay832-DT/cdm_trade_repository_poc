from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.template.extension_event import ExtensionEvent

class ExtendibleProvisionAdjustedDates(CdmModelBase):
    """A data defining:  the adjusted dates associated with a provision to extend a swap."""
    extension_event: List[ForwardRef("ExtensionEvent")] = Field(None, description="The adjusted dates associated with a single extendible exercise date.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.template.extension_event import ExtensionEvent
ExtendibleProvisionAdjustedDates.model_rebuild()
