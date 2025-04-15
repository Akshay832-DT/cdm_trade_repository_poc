from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class AveragingCalculationMethodEnum(CdmModelBase):
    """Specifies enumerations for the type of averaging calculation."""
    # Enum values
    Arithmetic: ClassVar[str] = "Arithmetic"
    Geometric: ClassVar[str] = "Geometric"
    Harmonic: ClassVar[str] = "Harmonic"


# Import after class definition to avoid circular imports
AveragingCalculationMethodEnum.model_rebuild()
