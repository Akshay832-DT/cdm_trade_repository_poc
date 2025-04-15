from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class NonNegativeStep(CdmModelBase):
    """A class defining a step date and non-negative step value pair. This step definitions are used to define varying rate or amount schedules, e.g. a notional amortisation or a step-up coupon schedule."""
    step_date: str = Field(description="The date on which the associated stepValue becomes effective. This day may be subject to adjustment in accordance with a business day convention.")
    step_value: float = Field(description="The non-negative rate or amount which becomes effective on the associated stepDate. A rate of 5% would be represented as 0.05.")

# Import after class definition to avoid circular imports
NonNegativeStep.model_rebuild()
