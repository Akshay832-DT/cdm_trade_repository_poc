from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class MarginCallResponseTypeEnum(CdmModelBase):
    """Represents the enumeration values to define the response type to a margin call."""
    # Enum values
    AgreeinFull: ClassVar[str] = "AgreeinFull"
    Dispute: ClassVar[str] = "Dispute"
    PartiallyAgree: ClassVar[str] = "PartiallyAgree"


# Import after class definition to avoid circular imports
MarginCallResponseTypeEnum.model_rebuild()
