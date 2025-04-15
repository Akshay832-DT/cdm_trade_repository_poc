from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class PeriodExtendedEnum(CdmModelBase):
    """The enumerated values to specify a time period containing the additional value of Term."""
    # Enum values
    C: ClassVar[str] = "C"
    D: ClassVar[str] = "D"
    H: ClassVar[str] = "H"
    M: ClassVar[str] = "M"
    T: ClassVar[str] = "T"
    W: ClassVar[str] = "W"
    Y: ClassVar[str] = "Y"


# Import after class definition to avoid circular imports
PeriodExtendedEnum.model_rebuild()
