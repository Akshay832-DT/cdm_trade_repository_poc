from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class LoadTypeEnum(CdmModelBase):
    """Specifies the load type of the delivery."""
    # Enum values
    BaseLoad: ClassVar[str] = "BaseLoad"
    BlockHours: ClassVar[str] = "BlockHours"
    GasDay: ClassVar[str] = "GasDay"
    OffPeak: ClassVar[str] = "OffPeak"
    Other: ClassVar[str] = "Other"
    PeakLoad: ClassVar[str] = "PeakLoad"
    Shaped: ClassVar[str] = "Shaped"


# Import after class definition to avoid circular imports
LoadTypeEnum.model_rebuild()
