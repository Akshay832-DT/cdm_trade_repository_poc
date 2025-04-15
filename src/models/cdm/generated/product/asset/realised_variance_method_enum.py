from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class RealisedVarianceMethodEnum(CdmModelBase):
    """The contract specifies which price must satisfy the boundary condition.  Used for variance, volatility and correlation caps and floors."""
    # Enum values
    Both: ClassVar[str] = "Both"
    Last: ClassVar[str] = "Last"
    Previous: ClassVar[str] = "Previous"


# Import after class definition to avoid circular imports
RealisedVarianceMethodEnum.model_rebuild()
