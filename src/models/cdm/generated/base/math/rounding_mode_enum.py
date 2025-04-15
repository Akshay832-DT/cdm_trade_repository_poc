from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class RoundingModeEnum(CdmModelBase):
    """The enumerated values to specify the rounding direction when rounding of a number to nearest.  Used by function cdm.base.math.RoundToNearest."""
    # Enum values
    Down: ClassVar[str] = "Down"
    Up: ClassVar[str] = "Up"


# Import after class definition to avoid circular imports
RoundingModeEnum.model_rebuild()
