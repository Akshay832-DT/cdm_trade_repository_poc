from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.party import Party
    from src.models.cdm.generated.event.common.billing_record_instruction import BillingRecordInstruction
    from src.models.cdm.generated.event.common.billing_summary_instruction import BillingSummaryInstruction

class BillingInstruction(CdmModelBase):
    """Specifies the instructions for creation of a Security Lending billing invoice."""
    sending_party: ForwardRef("Party") = Field(description="The party issuing the invoice")
    receiving_party: ForwardRef("Party") = Field(description="The party receiving the invoice")
    billing_start_date: str = Field(description="The starting date of the period described by this invoice")
    billing_end_date: str = Field(description="The ending date of the period described by this invoice")
    billing_record_instruction: List[ForwardRef("BillingRecordInstruction")] = Field(None, description="Instructions for creating the billing records contained within the invoice")
    billing_summary: List[ForwardRef("BillingSummaryInstruction")] = Field(None, description="The billing summaries contained within the invoice")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.party import Party
from src.models.cdm.generated.event.common.billing_record_instruction import BillingRecordInstruction
from src.models.cdm.generated.event.common.billing_summary_instruction import BillingSummaryInstruction
BillingInstruction.model_rebuild()
