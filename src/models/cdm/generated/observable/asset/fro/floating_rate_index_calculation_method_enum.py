from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class FloatingRateIndexCalculationMethodEnum(CdmModelBase):
    """3rd level ISDA FRO category."""
    # Enum values
    All_In_Compounded_Index: ClassVar[str] = "All-In Compounded Index"
    Overnight_Averaging: ClassVar[str] = "Overnight Averaging"
    Compounded_Index: ClassVar[str] = "Compounded Index"
    OIS_Compounding: ClassVar[str] = "OIS Compounding"


# Import after class definition to avoid circular imports
FloatingRateIndexCalculationMethodEnum.model_rebuild()
