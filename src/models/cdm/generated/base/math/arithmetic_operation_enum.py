from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class ArithmeticOperationEnum(CdmModelBase):
    """An arithmetic operator that can be passed to a function"""
    # Enum values
    Add: ClassVar[str] = "Add"
    Divide: ClassVar[str] = "Divide"
    Max: ClassVar[str] = "Max"
    Min: ClassVar[str] = "Min"
    Multiply: ClassVar[str] = "Multiply"
    Subtract: ClassVar[str] = "Subtract"


# Import after class definition to avoid circular imports
ArithmeticOperationEnum.model_rebuild()
