from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.math.rounding_direction_enum import RoundingDirectionEnum

class Rounding(CdmModelBase):
    """Defines rounding rules and precision to be used in the rounding of a number."""
    rounding_direction: ForwardRef("RoundingDirectionEnum") = Field(description="Specifies the rounding rounding rule as up, down, or nearest.")
    precision: int = Field(None, description="Specifies the rounding precision in terms of a number of decimal places when the number is evaluated in decimal form (not percentage), e.g. 0.09876543 rounded to the nearest 5 decimal places is  0.0987654.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.math.rounding_direction_enum import RoundingDirectionEnum
Rounding.model_rebuild()
