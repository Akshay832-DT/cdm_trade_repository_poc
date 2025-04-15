from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class PositionStatusEnum(CdmModelBase):
    """Enumeration to describe the different (risk) states of a Position, whether executed, settled, matured...etc"""
    # Enum values
    Cancelled: ClassVar[str] = "Cancelled"
    Closed: ClassVar[str] = "Closed"
    Executed: ClassVar[str] = "Executed"
    Formed: ClassVar[str] = "Formed"
    Settled: ClassVar[str] = "Settled"


# Import after class definition to avoid circular imports
PositionStatusEnum.model_rebuild()
