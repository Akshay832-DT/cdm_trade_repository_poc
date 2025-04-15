from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class PayerReceiverEnum(CdmModelBase):
    """The enumerated values to specify an interest rate stream payer or receiver party."""
    # Enum values
    Payer: ClassVar[str] = "Payer"
    Receiver: ClassVar[str] = "Receiver"


# Import after class definition to avoid circular imports
PayerReceiverEnum.model_rebuild()
