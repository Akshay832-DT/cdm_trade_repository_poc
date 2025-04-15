from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.rates.floating_rate_index_enum import FloatingRateIndexEnum
    from src.models.cdm.generated.observable.asset.calculatedrate.floating_rate_calculation_parameters import FloatingRateCalculationParameters

class FallbackRateParameters(CdmModelBase):
    """Defines the structure needed to represent fallback rate parameters. This type is used to represent modular computed rates in interestRatePayouts."""
    floating_rate_index: ForwardRef("FloatingRateIndexEnum") = Field(description="The floating rate index that is used as the basis of the fallback rate.")
    effective_date: str = Field(None, description="The date the fallback rate takes effect.")
    calculation_parameters: ForwardRef("FloatingRateCalculationParameters") = Field(None, description="Support for modular calculated rates, such such as lockout compound calculations.")
    spread_adjustment: float = Field(None, description="The economic spread applied to the underlying fallback rate to replicate the original risky rate.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.rates.floating_rate_index_enum import FloatingRateIndexEnum
from src.models.cdm.generated.observable.asset.calculatedrate.floating_rate_calculation_parameters import FloatingRateCalculationParameters
FallbackRateParameters.model_rebuild()
