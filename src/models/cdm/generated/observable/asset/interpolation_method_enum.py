from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class InterpolationMethodEnum(CdmModelBase):
    """The enumerated values to specify the method of interpolation."""
    # Enum values
    Linear: ClassVar[str] = "Linear"
    NoInterpolation: ClassVar[str] = "None"  # Renamed from None to NoInterpolation to avoid syntax error
    Logarithmic: ClassVar[str] = "Logarithmic"
    Cubic: ClassVar[str] = "Cubic"


# Import after class definition to avoid circular imports
InterpolationMethodEnum.model_rebuild()
