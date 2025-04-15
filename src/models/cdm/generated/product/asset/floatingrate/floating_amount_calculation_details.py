from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.money import Money
    from src.models.cdm.generated.product.asset.floatingrate.floating_rate_processing_details import FloatingRateProcessingDetails
    from src.models.cdm.generated.product.asset.floatingrate.floating_rate_setting_details import FloatingRateSettingDetails
    from src.models.cdm.generated.product.common.schedule.calculation_period_base import CalculationPeriodBase

class FloatingAmountCalculationDetails(CdmModelBase):
    """Type for reporting the detailed results of calculating a cash flow for a calculation period.  This is enhanced relative to the FpML-based cashflows structure to allow more information to be returned about daily compounded rates."""
    calculation_period: ForwardRef("CalculationPeriodBase") = Field(description="The calculation period for which the floating calculation was performed.")
    calculation_period_notional_amount: ForwardRef("Money") = Field(description="The notional in effect during the calculation period.")
    floating_rate: ForwardRef("FloatingRateSettingDetails") = Field(None, description="The details of the floating rate setting.  (If it is a calculated rate, details of that calculation will be inside that.")
    processing_details: ForwardRef("FloatingRateProcessingDetails") = Field(None, description="Details fo the floating rate treatment after the rate is observed or calculated.  This will include details of things like multipliers, spreads, caps and floors, and the raw and treated rates.")
    applied_rate: float = Field(description="The rate that was actually applied, after all calculations and treatments.")
    year_fraction: float = Field(description="The fraction of a year that this calculation represents, according to the day count fraction method.")
    calculated_amount: float = Field(description="The amount of the cash flow that was computed, including any spreads and other processing.")
    spread_exclusive_calculated_a_mount: float = Field(description="The amount of the cash flow excluding any spread, for subsequent processing.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.money import Money
from src.models.cdm.generated.product.asset.floatingrate.floating_rate_processing_details import FloatingRateProcessingDetails
from src.models.cdm.generated.product.asset.floatingrate.floating_rate_setting_details import FloatingRateSettingDetails
from src.models.cdm.generated.product.common.schedule.calculation_period_base import CalculationPeriodBase
FloatingAmountCalculationDetails.model_rebuild()
