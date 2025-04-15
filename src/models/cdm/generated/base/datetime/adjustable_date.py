from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.business_day_adjustments import BusinessDayAdjustments
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
    from src.models.cdm.generated.metafields.reference_with_meta_business_day_adjustments import ReferenceWithMetaBusinessDayAdjustments

class AdjustableDate(CdmModelBase):
    """A class for defining a date that shall be subject to adjustment if it would otherwise fall on a day that is not a business day in the specified business centers, together with the convention for adjusting the date."""
    unadjusted_date: str = Field(None, description="A date subject to adjustment. While in FpML this date is required, this cardinality constraint has been relaxed as part of the CDM in order to support the FRA representation, which effective and termination dates are specified in FpML as adjusted dates.")
    date_adjustments: ForwardRef("BusinessDayAdjustments") = Field(None, description="The business day convention and financial business centers used for adjusting the date if it would otherwise fall on a day that is not a business date in the specified business centers.")
    date_adjustments_reference: ForwardRef("ReferenceWithMetaBusinessDayAdjustments") = Field(None, description="A pointer style reference to date adjustments defined elsewhere in the document.")
    adjusted_date: ForwardRef("FieldWithMetaString") = Field(None, description="The date once the adjustment has been performed. (Note that this date may change if the business center holidays change).")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.business_day_adjustments import BusinessDayAdjustments
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
from src.models.cdm.generated.metafields.reference_with_meta_business_day_adjustments import ReferenceWithMetaBusinessDayAdjustments
AdjustableDate.model_rebuild()
