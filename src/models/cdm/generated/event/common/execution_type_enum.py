from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class ExecutionTypeEnum(CdmModelBase):
    """The enumerated values to specify how a contract has been executed, e.g. electronically, verbally, ..."""
    # Enum values
    Electronic: ClassVar[str] = "Electronic"
    OffFacility: ClassVar[str] = "OffFacility"
    OnVenue: ClassVar[str] = "OnVenue"


# Import after class definition to avoid circular imports
ExecutionTypeEnum.model_rebuild()
