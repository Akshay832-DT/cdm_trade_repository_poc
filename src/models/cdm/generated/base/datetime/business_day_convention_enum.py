from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class BusinessDayConventionEnum(CdmModelBase):
    """The enumerated values to specify the convention for adjusting any relevant date if it would otherwise fall on a day that is not a valid business day."""
    # Enum values
    FOLLOWING: ClassVar[str] = "FOLLOWING"
    FRN: ClassVar[str] = "FRN"
    MODFOLLOWING: ClassVar[str] = "MODFOLLOWING"
    MODPRECEDING: ClassVar[str] = "MODPRECEDING"
    NEAREST: ClassVar[str] = "NEAREST"
    NONE: ClassVar[str] = "NONE"
    NotApplicable: ClassVar[str] = "NotApplicable"
    PRECEDING: ClassVar[str] = "PRECEDING"


# Import after class definition to avoid circular imports
BusinessDayConventionEnum.model_rebuild()
