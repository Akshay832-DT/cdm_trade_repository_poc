from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class ActionEnum(CdmModelBase):
    """The enumeration values to specify the actions associated with transactions."""
    # Enum values
    Cancel: ClassVar[str] = "Cancel"
    Correct: ClassVar[str] = "Correct"
    New: ClassVar[str] = "New"


# Import after class definition to avoid circular imports
ActionEnum.model_rebuild()
