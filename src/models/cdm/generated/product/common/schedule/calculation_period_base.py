from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CalculationPeriodBase(CdmModelBase):
    """The calculation period adjusted start and end dates, which are the baseline arguments needed to compute an interest accrual calculation."""
    adjusted_start_date: str = Field(None, description="The calculation period start date, adjusted according to any relevant business day convention.")
    adjusted_end_date: str = Field(None, description="The calculation period end date, adjusted according to any relevant business day convention.")

# Import after class definition to avoid circular imports
CalculationPeriodBase.model_rebuild()
