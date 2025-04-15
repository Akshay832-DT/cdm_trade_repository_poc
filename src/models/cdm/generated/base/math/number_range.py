from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.math.number_bound import NumberBound

class NumberRange(CdmModelBase):
    """The number range defined as either a lower and upper number bound, or both."""
    lower_bound: ForwardRef("NumberBound") = Field(None, description="The lower bound of a number range, e.g. greater than or equal to 5.")
    upper_bound: ForwardRef("NumberBound") = Field(None, description="The upper bound of a number range, e.g. less than 10.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.math.number_bound import NumberBound
NumberRange.model_rebuild()
