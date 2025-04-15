from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.common.scheduled_transfer import ScheduledTransfer
    from src.models.cdm.generated.observable.asset.fee_type_enum import FeeTypeEnum

class TransferExpression(CdmModelBase):
    """Specifies a transfer expression (cash price, performance amount, scheduled payment amount, etc.) to define the nature of the transfer amount and its source."""
    price_transfer: ForwardRef("FeeTypeEnum") = Field(None, description="Specifies a transfer amount exchanged as a price or fee for entering into a Business Event, e.g. Premium, Termination fee, Novation fee.")
    scheduled_transfer: ForwardRef("ScheduledTransfer") = Field(None, description="Specifies a transfer created from a scheduled or contingent event on a contract, e.g. Exercise, Performance, Credit Event")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.common.scheduled_transfer import ScheduledTransfer
from src.models.cdm.generated.observable.asset.fee_type_enum import FeeTypeEnum
TransferExpression.model_rebuild()
