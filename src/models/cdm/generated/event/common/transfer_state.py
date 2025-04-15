from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.common.transfer import Transfer
    from src.models.cdm.generated.event.common.transfer_status_enum import TransferStatusEnum

class TransferState(CdmModelBase):
    """Defines the fundamental financial information associated with a Transfer event. Each TransferState specifies where a Transfer is in its life-cycle. TransferState is a root type and as such, can be created independently to any other CDM data type, but can also be used as part of the CDM Event Model."""
    transfer: ForwardRef("Transfer") = Field(description="Represents the Transfer that has been effected by a business or life-cycle event.")
    transfer_status: ForwardRef("TransferStatusEnum") = Field(None, description="Represents the State of the Transfer through its life-cycle.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.common.transfer import Transfer
from src.models.cdm.generated.event.common.transfer_status_enum import TransferStatusEnum
TransferState.model_rebuild()
