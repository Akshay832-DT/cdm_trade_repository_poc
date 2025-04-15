from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.common.record_amount_type_enum import RecordAmountTypeEnum
    from src.models.cdm.generated.event.common.transfer import Transfer

class BillingSummary(CdmModelBase):
    """Specifies individual summaries within a billing invoice."""
    summary_transfer: ForwardRef("Transfer") = Field(None, description="The settlement terms for the billing summary")
    summary_amount_type: ForwardRef("RecordAmountTypeEnum") = Field(description="The account level for the billing summary.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.common.record_amount_type_enum import RecordAmountTypeEnum
from src.models.cdm.generated.event.common.transfer import Transfer
BillingSummary.model_rebuild()
