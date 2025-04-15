from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class MandatoryEarlyTerminationAdjustedDates(CdmModelBase):
    """A data defining:  the adjusted dates associated with a mandatory early termination provision."""
    adjusted_early_termination_date: str = Field(description="The early termination date that is applicable if an early termination provision is exercised. This date should already be adjusted for any applicable business day convention.")
    adjusted_cash_settlement_valuation_date: str = Field(description="The date by which the cash settlement amount must be agreed. This date should already be adjusted for any applicable business day convention.")
    adjusted_cash_settlement_payment_date: str = Field(description="The date on which the cash settlement amount is paid. This date should already be adjusted for any applicable business date convention.")

# Import after class definition to avoid circular imports
MandatoryEarlyTerminationAdjustedDates.model_rebuild()
