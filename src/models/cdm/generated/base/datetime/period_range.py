from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.period_bound import PeriodBound

class PeriodRange(CdmModelBase):
    """Indicates The period range defined as either a lower and upper period bound, or both."""
    lower_bound: ForwardRef("PeriodBound") = Field(None, description="Specifies the lower bound of a period range, e.g. greater than or equal to 5Y.")
    upper_bound: ForwardRef("PeriodBound") = Field(None, description="Specifies the upper bound of a period range, e.g. less than to 10Y.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.period_bound import PeriodBound
PeriodRange.model_rebuild()
