from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class PutCallEnum(CdmModelBase):
    """The enumerated values to specify the types of listed derivative options."""
    # Enum values
    Call: ClassVar[str] = "Call"
    Put: ClassVar[str] = "Put"


# Import after class definition to avoid circular imports
PutCallEnum.model_rebuild()
