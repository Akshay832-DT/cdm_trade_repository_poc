from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.money import Money
    from src.models.cdm.generated.product.asset.floating_rate_definition import FloatingRateDefinition
    from src.models.cdm.generated.product.common.schedule.fx_linked_notional_amount import FxLinkedNotionalAmount

class CalculationPeriod(CdmModelBase):
    """A data defining:  the parameters used in the calculation of a fixed or floating rate calculation period amount. This data forms:  part of cashflows representation of a swap stream."""
    adjusted_start_date: str = Field(None, description="The calculation period start date, adjusted according to any relevant business day convention.")
    adjusted_end_date: str = Field(None, description="The calculation period end date, adjusted according to any relevant business day convention.")
    unadjusted_start_date: str = Field(None, description="The calculation start date, unadjusted.")
    unadjusted_end_date: str = Field(None, description="The calculation end date, unadjusted.")
    calculation_period_number_of_days: int = Field(None, description="The number of days from the adjusted effective / start date to the adjusted termination / end date calculated in accordance with the applicable day count fraction.")
    notional_amount: float = Field(None, description="The amount that a cashflow will accrue interest on.")
    fx_linked_notional_amount: ForwardRef("FxLinkedNotionalAmount") = Field(None, description="The amount that a cashflow will accrue interest on. This is the calculated amount of the FX linked - i.e. the other currency notional amount multiplied by the appropriate FX spot rate.")
    floating_rate_definition: ForwardRef("FloatingRateDefinition") = Field(None, description="The floating rate reset information for the calculation period.")
    fixed_rate: float = Field(None, description="The calculation period fixed rate. A per annum rate, expressed as a decimal. A fixed rate of 5% would be represented as 0.05.")
    day_count_year_fraction: float = Field(None, description="The year fraction value of the calculation period, result of applying the ISDA rules for day count fraction defined in the ISDA Annex.")
    forecast_amount: ForwardRef("Money") = Field(None, description="The amount representing the forecast of the accrued value of the calculation period. An intermediate value used to generate the forecastPaymentAmount in the PaymentCalculationPeriod.")
    forecast_rate: float = Field(None, description="A value representing the forecast rate used to calculate the forecast future value of the accrual period. This is a calculated rate determined based on averaging the rates in the rateObservation elements, and incorporates all of the rate treatment and averaging rules. A value of 1% should be represented as 0.01.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.money import Money
from src.models.cdm.generated.product.asset.floating_rate_definition import FloatingRateDefinition
from src.models.cdm.generated.product.common.schedule.fx_linked_notional_amount import FxLinkedNotionalAmount
CalculationPeriod.model_rebuild()
