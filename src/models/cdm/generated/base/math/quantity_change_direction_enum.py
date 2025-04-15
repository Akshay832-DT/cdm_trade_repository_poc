from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class QuantityChangeDirectionEnum(CdmModelBase):
    """Specifies whether a quantity change is an increase, a decrease or a replacement, whereby the quantity is always specified as a positive number."""
    # Enum values
    Decrease: ClassVar[str] = "Decrease"
    Increase: ClassVar[str] = "Increase"
    Replace: ClassVar[str] = "Replace"


# Import after class definition to avoid circular imports
QuantityChangeDirectionEnum.model_rebuild()
