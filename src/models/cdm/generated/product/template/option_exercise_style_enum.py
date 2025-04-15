from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class OptionExerciseStyleEnum(CdmModelBase):
    """The enumerated values to specify the option exercise style. i.e., European, Bermuda or American."""
    # Enum values
    American: ClassVar[str] = "American"
    Bermuda: ClassVar[str] = "Bermuda"
    European: ClassVar[str] = "European"


# Import after class definition to avoid circular imports
OptionExerciseStyleEnum.model_rebuild()
