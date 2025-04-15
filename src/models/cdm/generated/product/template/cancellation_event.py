from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CancellationEvent(CdmModelBase):
    """The adjusted dates for a specific cancellation date, including the adjusted exercise date and adjusted termination date."""
    adjusted_exercise_date: str = Field(description="The date on which option exercise takes place. This date should already be adjusted for any applicable business day convention.")
    adjusted_early_termination_date: str = Field(description="The early termination date that is applicable if an early termination provision is exercised. This date should already be adjusted for any applicable business day convention.")

# Import after class definition to avoid circular imports
CancellationEvent.model_rebuild()
