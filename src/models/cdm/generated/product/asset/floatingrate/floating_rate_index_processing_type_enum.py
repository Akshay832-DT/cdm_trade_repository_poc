from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class FloatingRateIndexProcessingTypeEnum(CdmModelBase):
    """This enumeration provides guidance on how to process a given floating rate index.  It's based on the ISDA Floating Rate Index information, but transforms it into the specific categories needed for calculation """
    # Enum values
    CompoundIndex: ClassVar[str] = "CompoundIndex"
    Modular: ClassVar[str] = "Modular"
    OIS: ClassVar[str] = "OIS"
    OvernightAvg: ClassVar[str] = "OvernightAvg"
    RefBanks: ClassVar[str] = "RefBanks"
    Screen: ClassVar[str] = "Screen"


# Import after class definition to avoid circular imports
FloatingRateIndexProcessingTypeEnum.model_rebuild()
