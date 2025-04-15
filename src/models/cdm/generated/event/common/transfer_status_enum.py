from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class TransferStatusEnum(CdmModelBase):
    """The enumeration values to specify the transfer status."""
    # Enum values
    Disputed: ClassVar[str] = "Disputed"
    Instructed: ClassVar[str] = "Instructed"
    Netted: ClassVar[str] = "Netted"
    Pending: ClassVar[str] = "Pending"
    Settled: ClassVar[str] = "Settled"


# Import after class definition to avoid circular imports
TransferStatusEnum.model_rebuild()
