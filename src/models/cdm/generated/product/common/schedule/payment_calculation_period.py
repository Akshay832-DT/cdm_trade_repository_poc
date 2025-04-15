from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.money import Money
    from src.models.cdm.generated.product.common.schedule.calculation_period import CalculationPeriod

class PaymentCalculationPeriod(CdmModelBase):
    """A data defining:  the adjusted payment date and associated calculation period parameters required to calculate the actual or projected payment amount. This data forms:  part of the cashflow representation of a swap stream."""
    unadjusted_payment_date: str = Field(None, description="The unadjusted payment date.")
    adjusted_payment_date: str = Field(None, description="The adjusted payment date. This date should already be adjusted for any applicable business day convention. This component is not intended for use in trade confirmation but may be specified to allow the fee structure to also serve as a cashflow type component.")
    calculation_period: List[ForwardRef("CalculationPeriod")] = Field(None, description="The parameters used in the calculation of a fixed or floating rate calculation period amount. A list of calculation period elements may be ordered in the document by ascending start date. An FpML document which contains an unordered list of calculation periods is still regarded as a conformant document.")
    fixed_payment_amount: ForwardRef("Money") = Field(None, description="A known fixed payment amount.")
    discount_factor: float = Field(None, description="A decimal value representing the discount factor used to calculate the present value of cash flow.")
    forecast_payment_amount: ForwardRef("Money") = Field(None, description="A monetary amount representing the forecast of the future value of the payment.")
    present_value_amount: ForwardRef("Money") = Field(None, description="A monetary amount representing the present value of the forecast payment.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.money import Money
from src.models.cdm.generated.product.common.schedule.calculation_period import CalculationPeriod
PaymentCalculationPeriod.model_rebuild()
