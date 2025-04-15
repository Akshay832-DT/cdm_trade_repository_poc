from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CompoundingMethodEnum(CdmModelBase):
    """The enumerated values to specify the type of compounding, e.g. flat, straight."""
    # Enum values
    Flat: ClassVar[str] = "Flat"
    NoCompounding: ClassVar[str] = "None"
    SpreadExclusive: ClassVar[str] = "SpreadExclusive"
    Straight: ClassVar[str] = "Straight"


# Import after class definition to avoid circular imports
CompoundingMethodEnum.model_rebuild()
