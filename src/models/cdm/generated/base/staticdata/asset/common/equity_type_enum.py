from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class EquityTypeEnum(CdmModelBase):
    """Represents an enumeration list to identify the type of Equity."""
    # Enum values
    NonConvertiblePreference: ClassVar[str] = "NonConvertiblePreference"
    Ordinary: ClassVar[str] = "Ordinary"


# Import after class definition to avoid circular imports
EquityTypeEnum.model_rebuild()
