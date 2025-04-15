from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class EarlyTerminationEvent(CdmModelBase):
    """A data to:  define the adjusted dates associated with an early termination provision."""
    adjusted_exercise_date: str = Field(description="The date on which option exercise takes place. This date should already be adjusted for any applicable business day convention.")
    adjusted_early_termination_date: str = Field(description="The early termination date that is applicable if an early termination provision is exercised. This date should already be adjusted for any applicable business day convention.")
    adjusted_cash_settlement_valuation_date: str = Field(description="The date by which the cash settlement amount must be agreed. This date should already be adjusted for any applicable business day convention.")
    adjusted_cash_settlement_payment_date: str = Field(description="The date on which the cash settlement amount is paid. This date should already be adjusted for any applicable business date convention.")
    adjusted_exercise_fee_payment_date: str = Field(None, description="The date on which the exercise fee amount is paid. This date should already be adjusted for any applicable business day convention.")

# Import after class definition to avoid circular imports
EarlyTerminationEvent.model_rebuild()
