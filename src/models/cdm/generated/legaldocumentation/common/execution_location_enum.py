from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class ExecutionLocationEnum(CdmModelBase):
    """The enumerated values to specify the Execution Location of a Security Agreement"""
    # Enum values
    ExecutedInBelgium: ClassVar[str] = "ExecutedInBelgium"
    ExecutedOutsideBelgium: ClassVar[str] = "ExecutedOutsideBelgium"
    OtherLocation: ClassVar[str] = "OtherLocation"


# Import after class definition to avoid circular imports
ExecutionLocationEnum.model_rebuild()
