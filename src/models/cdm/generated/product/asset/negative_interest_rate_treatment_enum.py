from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class NegativeInterestRateTreatmentEnum(CdmModelBase):
    """The enumerated values to specify the method of calculating payment obligations when a floating rate is negative (either due to a quoted negative floating rate or by operation of a spread that is subtracted from the floating rate)."""
    # Enum values
    NegativeInterestRateMethod: ClassVar[str] = "NegativeInterestRateMethod"
    ZeroInterestRateExcludingSpreadMethod: ClassVar[str] = "ZeroInterestRateExcludingSpreadMethod"
    ZeroInterestRateMethod: ClassVar[str] = "ZeroInterestRateMethod"


# Import after class definition to avoid circular imports
NegativeInterestRateTreatmentEnum.model_rebuild()
