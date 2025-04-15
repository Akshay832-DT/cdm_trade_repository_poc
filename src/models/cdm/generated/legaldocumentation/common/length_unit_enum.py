from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class LengthUnitEnum(CdmModelBase):
    """The enumerated values to specify the length unit in the Resource type."""
    # Enum values
    Pages: ClassVar[str] = "Pages"
    TimeUnit: ClassVar[str] = "TimeUnit"


# Import after class definition to avoid circular imports
LengthUnitEnum.model_rebuild()
