from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class OptionTypeEnum(CdmModelBase):
    """The enumerated values to specify the type or strategy of the option."""
    # Enum values
    Call: ClassVar[str] = "Call"
    Payer: ClassVar[str] = "Payer"
    Put: ClassVar[str] = "Put"
    Receiver: ClassVar[str] = "Receiver"
    Straddle: ClassVar[str] = "Straddle"


# Import after class definition to avoid circular imports
OptionTypeEnum.model_rebuild()
