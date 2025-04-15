from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class RoundingFrequencyEnum(CdmModelBase):
    """How often is rounding performed"""
    # Enum values
    Daily: ClassVar[str] = "Daily"
    PeriodEnd: ClassVar[str] = "PeriodEnd"


# Import after class definition to avoid circular imports
RoundingFrequencyEnum.model_rebuild()
