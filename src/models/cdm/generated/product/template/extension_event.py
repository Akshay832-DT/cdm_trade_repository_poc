from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class ExtensionEvent(CdmModelBase):
    """A data to:  define the adjusted dates associated with an individual extension event."""
    adjusted_exercise_date: str = Field(description="The date on which option exercise takes place. This date should already be adjusted for any applicable business day convention.")
    adjusted_extended_termination_date: str = Field(description="The termination date if an extendible provision is exercised. This date should already be adjusted for any applicable business day convention.")

# Import after class definition to avoid circular imports
ExtensionEvent.model_rebuild()
