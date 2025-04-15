from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CalculationMethodEnum(CdmModelBase):
    """What calculation type is required, averaging or compounding. This enumeration is used to represent the definitions of modular calculated rates as described in the 2021 ISDA Definitions, section 7."""
    # Enum values
    Averaging: ClassVar[str] = "Averaging"
    CompoundedIndex: ClassVar[str] = "CompoundedIndex"
    Compounding: ClassVar[str] = "Compounding"


# Import after class definition to avoid circular imports
CalculationMethodEnum.model_rebuild()
