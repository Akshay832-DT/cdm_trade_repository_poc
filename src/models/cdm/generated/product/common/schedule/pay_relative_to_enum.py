from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class PayRelativeToEnum(CdmModelBase):
    """The enumerated values to specify whether payments occur relative to the calculation period start date or end date, each reset date, valuation date or the last pricing date."""
    # Enum values
    CalculationPeriodEndDate: ClassVar[str] = "CalculationPeriodEndDate"
    CalculationPeriodStartDate: ClassVar[str] = "CalculationPeriodStartDate"
    LastPricingDate: ClassVar[str] = "LastPricingDate"
    ResetDate: ClassVar[str] = "ResetDate"
    ValuationDate: ClassVar[str] = "ValuationDate"


# Import after class definition to avoid circular imports
PayRelativeToEnum.model_rebuild()
