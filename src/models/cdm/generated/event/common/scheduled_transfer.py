from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.common.corporate_action_type_enum import CorporateActionTypeEnum
    from src.models.cdm.generated.product.common.settlement.scheduled_transfer_enum import ScheduledTransferEnum

class ScheduledTransfer(CdmModelBase):
    """"""
    transfer_type: ForwardRef("ScheduledTransferEnum") = Field(description="Specifies a transfer created from a scheduled or contingent event on a contract, e.g. Exercise, Performance, Credit Event")
    corporate_action_transfer_type: ForwardRef("CorporateActionTypeEnum") = Field(None)

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.common.corporate_action_type_enum import CorporateActionTypeEnum
from src.models.cdm.generated.product.common.settlement.scheduled_transfer_enum import ScheduledTransferEnum
ScheduledTransfer.model_rebuild()
