from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class ExerciseEvent(CdmModelBase):
    """A data defining:  the adjusted dates associated with a particular exercise event."""
    adjusted_exercise_date: str = Field(description="The date on which the option exercise takes place. This date should already be adjusted for any applicable business day convention.")
    adjusted_relevant_swap_effective_date: str = Field(description="The effective date of the underlying swap associated with a given exercise date. This date should already be adjusted for any applicable business day convention.")
    adjusted_cash_settlement_valuation_date: str = Field(None, description="The date by which the cash settlement amount must be agreed. This date should already be adjusted for any applicable business day convention.")
    adjusted_cash_settlement_payment_date: str = Field(None, description="The date on which the cash settlement amount is paid. This date should already be adjusted for any applicable business day convention.")
    adjusted_exercise_fee_payment_date: str = Field(None, description="The date on which the exercise fee amount is paid. This date should already be adjusted for any applicable business day convention.")

# Import after class definition to avoid circular imports
ExerciseEvent.model_rebuild()
