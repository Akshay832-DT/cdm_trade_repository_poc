from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class DatedValue(CdmModelBase):
    """Defines a date and value pair. This definition is used for varying rate or amount schedules, e.g. a notional amortisation or a step-up coupon schedule."""
    date: str = Field(description="The date on which the associated step value becomes effective. This day may be subject to adjustment in accordance with a business day convention.")
    value: float = Field(description="The rate of amount which becomes effective on the associated step date. A rate of 5% would be represented as 0.05.")

# Import after class definition to avoid circular imports
DatedValue.model_rebuild()
