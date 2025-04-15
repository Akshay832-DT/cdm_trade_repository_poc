from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class DayDistributionEnum(CdmModelBase):
    """Denotes the method by which the pricing days are distributed across the pricing period."""
    # Enum values
    All: ClassVar[str] = "All"
    First: ClassVar[str] = "First"
    Last: ClassVar[str] = "Last"
    Penultimate: ClassVar[str] = "Penultimate"


# Import after class definition to avoid circular imports
DayDistributionEnum.model_rebuild()
