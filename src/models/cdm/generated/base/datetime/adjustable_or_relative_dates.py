from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.adjustable_dates import AdjustableDates
    from src.models.cdm.generated.base.datetime.relative_dates import RelativeDates

class AdjustableOrRelativeDates(CdmModelBase):
    """A class giving the choice between defining a series of dates as an explicit list of dates together with applicable adjustments or as relative to some other series of (anchor) dates."""
    adjustable_dates: ForwardRef("AdjustableDates") = Field(None, description="A series of dates that shall be subject to adjustment if they would otherwise fall on a day that is not a business day in the specified business centers, together with the convention for adjusting the date.")
    relative_dates: ForwardRef("RelativeDates") = Field(None, description="A series of dates specified as some offset to another series of dates (the anchor dates).")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.adjustable_dates import AdjustableDates
from src.models.cdm.generated.base.datetime.relative_dates import RelativeDates
AdjustableOrRelativeDates.model_rebuild()
