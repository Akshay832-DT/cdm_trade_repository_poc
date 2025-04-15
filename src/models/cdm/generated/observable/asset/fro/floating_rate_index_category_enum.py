from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class FloatingRateIndexCategoryEnum(CdmModelBase):
    """Top level ISDA FRO category."""
    # Enum values
    Calculated_Rate: ClassVar[str] = "Calculated Rate"
    Reference_Banks_Rate: ClassVar[str] = "Reference Banks Rate"
    Screen_Rate: ClassVar[str] = "Screen Rate"


# Import after class definition to avoid circular imports
FloatingRateIndexCategoryEnum.model_rebuild()
