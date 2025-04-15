from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class StubPeriodTypeEnum(CdmModelBase):
    """The enumerated values to specify how to deal with a non standard calculation period within a swap stream."""
    # Enum values
    LongFinal: ClassVar[str] = "LongFinal"
    LongInitial: ClassVar[str] = "LongInitial"
    ShortFinal: ClassVar[str] = "ShortFinal"
    ShortInitial: ClassVar[str] = "ShortInitial"


# Import after class definition to avoid circular imports
StubPeriodTypeEnum.model_rebuild()
