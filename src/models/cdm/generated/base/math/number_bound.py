from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class NumberBound(CdmModelBase):
    """The number bound is defined as a number and whether the bound is inclusive."""
    number: float = Field(description="The number to be used as the bound, e.g. 5.")
    inclusive: bool = Field(description="Whether the number bound is inclusive, e.g. for a lower bound, false would indicate greater than, whereas true would indicate greater than or equal to.")

# Import after class definition to avoid circular imports
NumberBound.model_rebuild()
