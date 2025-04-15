from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.reference_with_meta_calculation_period_dates import ReferenceWithMetaCalculationPeriodDates

class DateRelativeToCalculationPeriodDates(CdmModelBase):
    """A data to:  provide the ability to point to multiple payment nodes in the document through the unbounded paymentDatesReference."""
    calculation_period_dates_reference: List[ForwardRef("ReferenceWithMetaCalculationPeriodDates")] = Field(None, description="A set of href pointers to calculation period dates defined somewhere else in the document.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.reference_with_meta_calculation_period_dates import ReferenceWithMetaCalculationPeriodDates
DateRelativeToCalculationPeriodDates.model_rebuild()
