from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class FloatingRateIndexStyleEnum(CdmModelBase):
    """Second level ISDA FRO category."""
    # Enum values
    Average_FRO: ClassVar[str] = "Average FRO"
    Compounded_FRO: ClassVar[str] = "Compounded FRO"
    Compounded_Index: ClassVar[str] = "Compounded Index"
    Index: ClassVar[str] = "Index"
    Other: ClassVar[str] = "Other"
    Overnight_Rate: ClassVar[str] = "Overnight Rate"
    Published_Average_Rate: ClassVar[str] = "Published Average Rate"
    Specified_Formula: ClassVar[str] = "Specified Formula"
    Swap_Rate: ClassVar[str] = "Swap Rate"
    Term_Rate: ClassVar[str] = "Term Rate"


# Import after class definition to avoid circular imports
FloatingRateIndexStyleEnum.model_rebuild()
