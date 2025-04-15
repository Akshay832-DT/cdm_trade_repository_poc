from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.math.rounding import Rounding
    from src.models.cdm.generated.observable.asset.price import Price
    from src.models.cdm.generated.product.asset.negative_interest_rate_treatment_enum import NegativeInterestRateTreatmentEnum
    from src.models.cdm.generated.product.asset.rate_treatment_enum import RateTreatmentEnum

class FloatingRateProcessingParameters(CdmModelBase):
    """Type to hold the processing parameters that should be or were used to calculate a floating amount.  These parameters can vary over a schedule so this type holds the acutal values applicable to this calculation."""
    initial_rate: ForwardRef("Price") = Field(None, description="The rate to be applied for the initial period.")
    multiplier: float = Field(None, description="floating rate multiplier.")
    spread: float = Field(None, description="spread to be added to the floating rate.")
    treatment: ForwardRef("RateTreatmentEnum") = Field(None, description="US rate treatment (Bond Equivalent Yield or Money Market Yield, if applicable.")
    cap_rate: float = Field(None, description="capt to be applied to the floating rate.")
    floor_rate: float = Field(None, description="floor to be applied to the floating rate.")
    rounding: ForwardRef("Rounding") = Field(None, description="THe final rate rounding to be applied.")
    negative_treatment: ForwardRef("NegativeInterestRateTreatmentEnum") = Field(None, description="How to handle negative interest rates.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.math.rounding import Rounding
from src.models.cdm.generated.observable.asset.price import Price
from src.models.cdm.generated.product.asset.negative_interest_rate_treatment_enum import NegativeInterestRateTreatmentEnum
from src.models.cdm.generated.product.asset.rate_treatment_enum import RateTreatmentEnum
FloatingRateProcessingParameters.model_rebuild()
