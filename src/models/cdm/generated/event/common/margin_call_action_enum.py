from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class MarginCallActionEnum(CdmModelBase):
    """Represents the enumeration values to identify the collateral action instruction."""
    # Enum values
    Delivery: ClassVar[str] = "Delivery"
    Return: ClassVar[str] = "Return"


# Import after class definition to avoid circular imports
MarginCallActionEnum.model_rebuild()
