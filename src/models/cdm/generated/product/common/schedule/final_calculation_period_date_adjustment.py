from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.business_day_convention_enum import BusinessDayConventionEnum
    from src.models.cdm.generated.metafields.reference_with_meta_adjustable_or_relative_dates import ReferenceWithMetaAdjustableOrRelativeDates
    from src.models.cdm.generated.metafields.reference_with_meta_interest_rate_payout import ReferenceWithMetaInterestRatePayout

class FinalCalculationPeriodDateAdjustment(CdmModelBase):
    """A data to:  define business date convention adjustment to final payment period per leg."""
    relevant_underlying_date_reference: ForwardRef("ReferenceWithMetaAdjustableOrRelativeDates") = Field(description="Reference to the unadjusted cancellation effective dates.")
    swap_stream_reference: ForwardRef("ReferenceWithMetaInterestRatePayout") = Field(description="Reference to the leg, where date adjustments may apply.")
    business_day_convention: ForwardRef("BusinessDayConventionEnum") = Field(description="Override business date convention. This takes precedence over leg level information.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.business_day_convention_enum import BusinessDayConventionEnum
from src.models.cdm.generated.metafields.reference_with_meta_adjustable_or_relative_dates import ReferenceWithMetaAdjustableOrRelativeDates
from src.models.cdm.generated.metafields.reference_with_meta_interest_rate_payout import ReferenceWithMetaInterestRatePayout
FinalCalculationPeriodDateAdjustment.model_rebuild()
