from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.business_centers import BusinessCenters
    from src.models.cdm.generated.observable.asset.calculatedrate.calculation_method_enum import CalculationMethodEnum
    from src.models.cdm.generated.observable.asset.calculatedrate.observation_parameters import ObservationParameters
    from src.models.cdm.generated.observable.asset.calculatedrate.observation_shift_calculation import ObservationShiftCalculation
    from src.models.cdm.generated.observable.asset.calculatedrate.offset_calculation import OffsetCalculation

class FloatingRateCalculationParameters(CdmModelBase):
    """Defines the structures needed to represent the calculation parameters for daily averaged and compounded modular rates as defined in the 2021 ISDA Definitions in Section 7. This type is used to represent modular computed rates in interestRatePayouts."""
    calculation_method: ForwardRef("CalculationMethodEnum") = Field(description="calculation type (averaging or compounding).")
    observation_shift_calculation: ForwardRef("ObservationShiftCalculation") = Field(None, description="any obervation shift parameters if applicable.")
    lookback_calculation: ForwardRef("OffsetCalculation") = Field(None, description="any lookback  parameters if applicable.")
    lockout_calculation: ForwardRef("OffsetCalculation") = Field(None, description="any lockout  parameters if applicable.")
    applicable_business_days: ForwardRef("BusinessCenters") = Field(None, description="the business days that are applicable for the calculation.")
    observation_parameters: ForwardRef("ObservationParameters") = Field(None, description=" any applicable observation parameters, such as daily caps or floors.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.business_centers import BusinessCenters
from src.models.cdm.generated.observable.asset.calculatedrate.calculation_method_enum import CalculationMethodEnum
from src.models.cdm.generated.observable.asset.calculatedrate.observation_parameters import ObservationParameters
from src.models.cdm.generated.observable.asset.calculatedrate.observation_shift_calculation import ObservationShiftCalculation
from src.models.cdm.generated.observable.asset.calculatedrate.offset_calculation import OffsetCalculation
FloatingRateCalculationParameters.model_rebuild()
