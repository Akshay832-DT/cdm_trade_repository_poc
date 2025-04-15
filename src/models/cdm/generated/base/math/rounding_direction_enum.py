from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class RoundingDirectionEnum(CdmModelBase):
    """The enumerated values to specify the rounding direction and precision to be used in the rounding of a number.  Used by function cdm.base.math.RoundToPrecision."""
    # Enum values
    Down: ClassVar[str] = "Down"
    Nearest: ClassVar[str] = "Nearest"
    Up: ClassVar[str] = "Up"


# Import after class definition to avoid circular imports
RoundingDirectionEnum.model_rebuild()
