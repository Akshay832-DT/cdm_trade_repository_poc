from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class RestructuringEnum(CdmModelBase):
    """The enumerated values to specify the form of the restructuring credit event that is applicable to the credit default swap."""
    # Enum values
    ModModR: ClassVar[str] = "ModModR"
    ModR: ClassVar[str] = "ModR"
    R: ClassVar[str] = "R"


# Import after class definition to avoid circular imports
RestructuringEnum.model_rebuild()
