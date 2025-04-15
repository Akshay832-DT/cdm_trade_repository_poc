from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.party import Party
    from src.models.cdm.generated.event.common.billing_record import BillingRecord
    from src.models.cdm.generated.event.common.billing_summary import BillingSummary

class SecurityLendingInvoice(CdmModelBase):
    """Specifies the information required for inclusion in a securities lending billing invoice."""
    sending_party: ForwardRef("Party") = Field(description="The party issuing the invoice")
    receiving_party: ForwardRef("Party") = Field(description="The party receiving the invoice")
    billing_start_date: str = Field(description="The starting date of the period described by this invoice")
    billing_end_date: str = Field(description="The ending date of the period described by this invoice")
    billing_record: List[ForwardRef("BillingRecord")] = Field(None, description="The billing records contained within the invoice")
    billing_summary: List[ForwardRef("BillingSummary")] = Field(None, description="The billing summaries contained within the invoice")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.party import Party
from src.models.cdm.generated.event.common.billing_record import BillingRecord
from src.models.cdm.generated.event.common.billing_summary import BillingSummary
SecurityLendingInvoice.model_rebuild()
