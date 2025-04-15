from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.reference_with_meta_performance_valuation_dates import ReferenceWithMetaPerformanceValuationDates

class DateRelativeToValuationDates(CdmModelBase):
    """A data to:  provide the ability to point to multiple payment nodes in the document through the unbounded paymentDatesReference."""
    valuation_dates_reference: List[ForwardRef("ReferenceWithMetaPerformanceValuationDates")] = Field(None, description="A set of href pointers to valuation period dates defined somewhere else in the document.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.reference_with_meta_performance_valuation_dates import ReferenceWithMetaPerformanceValuationDates
DateRelativeToValuationDates.model_rebuild()
