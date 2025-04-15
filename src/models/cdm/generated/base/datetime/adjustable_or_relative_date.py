from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.adjustable_date import AdjustableDate
    from src.models.cdm.generated.base.datetime.adjusted_relative_date_offset import AdjustedRelativeDateOffset

class AdjustableOrRelativeDate(CdmModelBase):
    """A class giving the choice between defining a date as an explicit date together with applicable adjustments or as relative to some other (anchor) date."""
    adjustable_date: ForwardRef("AdjustableDate") = Field(None, description="A date that shall be subject to adjustment if it would otherwise fall on a day that is not a business day in the specified business centers, together with the convention for adjusting the date.")
    relative_date: ForwardRef("AdjustedRelativeDateOffset") = Field(None, description="A date specified as some offset to another date (the anchor date).")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.adjustable_date import AdjustableDate
from src.models.cdm.generated.base.datetime.adjusted_relative_date_offset import AdjustedRelativeDateOffset
AdjustableOrRelativeDate.model_rebuild()
