from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class PriceOperandEnum(CdmModelBase):
    """"""
    # Enum values
    AccruedInterest: ClassVar[str] = "AccruedInterest"
    Commission: ClassVar[str] = "Commission"
    ForwardPoint: ClassVar[str] = "ForwardPoint"


# Import after class definition to avoid circular imports
PriceOperandEnum.model_rebuild()
