from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.reference_with_meta_payment_dates import ReferenceWithMetaPaymentDates

class DateRelativeToPaymentDates(CdmModelBase):
    """A data to:  provide the ability to point to multiple payment nodes in the document through the unbounded paymentDatesReference."""
    payment_dates_reference: List[ForwardRef("ReferenceWithMetaPaymentDates")] = Field(None, description="A set of href pointers to payment dates defined somewhere else in the document.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.reference_with_meta_payment_dates import ReferenceWithMetaPaymentDates
DateRelativeToPaymentDates.model_rebuild()
