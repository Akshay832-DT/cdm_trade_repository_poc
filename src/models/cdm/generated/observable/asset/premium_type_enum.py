from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class PremiumTypeEnum(CdmModelBase):
    """The enumerated values to specify the premium type for forward start options."""
    # Enum values
    Fixed: ClassVar[str] = "Fixed"
    PostPaid: ClassVar[str] = "PostPaid"
    PrePaid: ClassVar[str] = "PrePaid"
    Variable: ClassVar[str] = "Variable"


# Import after class definition to avoid circular imports
PremiumTypeEnum.model_rebuild()
