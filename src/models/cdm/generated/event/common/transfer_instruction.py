from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.common.transfer_state import TransferState

class TransferInstruction(CdmModelBase):
    """Defines the payout on which to create a Transfer along with all necessary resets."""
    transfer_state: List[ForwardRef("TransferState")] = Field(None, description="Specifies the terms and state of a transfers.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.common.transfer_state import TransferState
TransferInstruction.model_rebuild()
