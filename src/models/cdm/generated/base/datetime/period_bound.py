from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.period import Period

class PeriodBound(CdmModelBase):
    """Indicator to specify if the period bound is defined as a period and whether the bound is inclusive."""
    period: ForwardRef("Period") = Field(description="Specifies the period is to be used as the bound, e.g. 5Y.")
    inclusive: bool = Field(description="Specifies whether the period bound is inclusive, e.g. for a lower bound, false would indicate greater than, whereas true would indicate greater than or equal to.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.period import Period
PeriodBound.model_rebuild()
