from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.money import Money
    from src.models.cdm.generated.product.common.schedule.calculation_period_base import CalculationPeriodBase

class FixedAmountCalculationDetails(CdmModelBase):
    """Type for reporting the detailed results of calculating a cash flow for a calculation period.  This is enhanced relative to the FpML-based cashflows structure to allow more information to be returned about daily compounded rates."""
    calculation_period: ForwardRef("CalculationPeriodBase") = Field(description="The calculation period for which the floating calculation was performed.")
    calculation_period_notional_amount: ForwardRef("Money") = Field(description="The notional in effect during the calculation period.")
    fixed_rate: float = Field(description="The value of the fixed rate that was used.")
    year_fraction: float = Field(description="The fraction of a year that this calculation represents, according to the day count fraction method.")
    calculated_amount: float = Field(description="The amount of the cash flow that was computed, including any spreads and other processing.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.money import Money
from src.models.cdm.generated.product.common.schedule.calculation_period_base import CalculationPeriodBase
FixedAmountCalculationDetails.model_rebuild()
