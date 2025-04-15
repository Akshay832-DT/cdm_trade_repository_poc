from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class ConfirmationStatusEnum(CdmModelBase):
    """Enumeration for the different types of confirmation status."""
    # Enum values
    Confirmed: ClassVar[str] = "Confirmed"
    Unconfirmed: ClassVar[str] = "Unconfirmed"


# Import after class definition to avoid circular imports
ConfirmationStatusEnum.model_rebuild()
