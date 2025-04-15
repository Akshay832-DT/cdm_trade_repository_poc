from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class SpreadScheduleTypeEnum(CdmModelBase):
    """The enumerated values to specify a long or short spread value."""
    # Enum values
    Long: ClassVar[str] = "Long"
    Short: ClassVar[str] = "Short"


# Import after class definition to avoid circular imports
SpreadScheduleTypeEnum.model_rebuild()
