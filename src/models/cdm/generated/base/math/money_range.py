from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.math.money_bound import MoneyBound

class MoneyRange(CdmModelBase):
    """The money range defined as either a lower and upper money bound, or both."""
    lower_bound: ForwardRef("MoneyBound") = Field(None, description="The lower bound of a money range, e.g. greater than or equal to 1,000 USD.")
    upper_bound: ForwardRef("MoneyBound") = Field(None, description="The upper bound of a money range, e.g. less than 10,000 USD.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.math.money_bound import MoneyBound
MoneyRange.model_rebuild()
