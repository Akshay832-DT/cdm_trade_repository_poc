from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class MaturityTypeEnum(CdmModelBase):
    """Represents an enumeration list to identify the Maturity."""
    # Enum values
    FromIssuance: ClassVar[str] = "FromIssuance"
    OriginalMaturity: ClassVar[str] = "OriginalMaturity"
    RemainingMaturity: ClassVar[str] = "RemainingMaturity"


# Import after class definition to avoid circular imports
MaturityTypeEnum.model_rebuild()
