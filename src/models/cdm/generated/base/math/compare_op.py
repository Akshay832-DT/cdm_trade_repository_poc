from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CompareOp(CdmModelBase):
    """"""
    # Enum values
    Equals: ClassVar[str] = "Equals"
    GreaterThan: ClassVar[str] = "GreaterThan"
    GreaterThanOrEquals: ClassVar[str] = "GreaterThanOrEquals"
    LessThan: ClassVar[str] = "LessThan"
    LessThanOrEquals: ClassVar[str] = "LessThanOrEquals"


# Import after class definition to avoid circular imports
CompareOp.model_rebuild()
