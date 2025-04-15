from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class ResetRelativeToEnum(CdmModelBase):
    """The enumerated values to specify whether resets occur relative to the first or last day of a calculation period."""
    # Enum values
    CalculationPeriodEndDate: ClassVar[str] = "CalculationPeriodEndDate"
    CalculationPeriodStartDate: ClassVar[str] = "CalculationPeriodStartDate"


# Import after class definition to avoid circular imports
ResetRelativeToEnum.model_rebuild()
