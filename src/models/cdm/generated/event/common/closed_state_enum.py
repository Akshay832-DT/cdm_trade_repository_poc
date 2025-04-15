from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class ClosedStateEnum(CdmModelBase):
    """The enumerated values to specify what led to the contract or execution closure."""
    # Enum values
    Allocated: ClassVar[str] = "Allocated"
    Cancelled: ClassVar[str] = "Cancelled"
    Exercised: ClassVar[str] = "Exercised"
    Expired: ClassVar[str] = "Expired"
    Matured: ClassVar[str] = "Matured"
    Novated: ClassVar[str] = "Novated"
    Terminated: ClassVar[str] = "Terminated"


# Import after class definition to avoid circular imports
ClosedStateEnum.model_rebuild()
