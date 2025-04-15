from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class AutomaticExercise(CdmModelBase):
    """A type to define automatic exercise of a swaption. With automatic exercise the option is deemed to have exercised if it is in the money by more than the threshold amount on the exercise date."""
    threshold_rate: float = Field(None, description="A threshold rate. The threshold of 0.10% would be represented as 0.001")
    is_applicable: bool = Field(None, description="Boolean that indicates if it has an automaticExercise")

# Import after class definition to avoid circular imports
AutomaticExercise.model_rebuild()
