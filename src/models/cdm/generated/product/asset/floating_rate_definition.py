from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.rate_observation import RateObservation
    from src.models.cdm.generated.product.template.strike import Strike

class FloatingRateDefinition(CdmModelBase):
    """A data defining:  parameters associated with a floating rate reset. This data forms:  part of the cashflows representation of a stream."""
    calculated_rate: float = Field(None, description="The final calculated rate for a calculation period after any required averaging of rates A calculated rate of 5% would be represented as 0.05.")
    rate_observation: List[ForwardRef("RateObservation")] = Field(None, description="The details of a particular rate observation, including the fixing date and observed rate. A list of rate observation elements may be ordered in the document by ascending adjusted fixing date. An FpML document containing an unordered list of rate observations is still regarded as a conformant document.")
    floating_rate_multiplier: float = Field(None, description="A rate multiplier to apply to the floating rate. The multiplier can be a positive or negative decimal. This element should only be included if the multiplier is not equal to 1 (one).")
    spread: float = Field(None, description="The ISDA Spread, if any, which applies for the calculation period. The spread is a per annum rate, expressed as a decimal. For purposes of determining a calculation period amount, if positive the spread will be added to the floating rate and if negative the spread will be subtracted from the floating rate. A positive 10 basis point (0.1%) spread would be represented as 0.001.")
    cap_rate: List[ForwardRef("Strike")] = Field(None, description="The cap rate, if any, which applies to the floating rate for the calculation period. The cap rate (strike) is only required where the floating rate on a swap stream is capped at a certain strike level. The cap rate is assumed to be exclusive of any spread and is a per annum rate, expressed as a decimal. A cap rate of 5% would be represented as 0.05.")
    floor_rate: List[ForwardRef("Strike")] = Field(None, description="The floor rate, if any, which applies to the floating rate for the calculation period. The floor rate (strike) is only required where the floating rate on a swap stream is floored at a certain strike level. The floor rate is assumed to be exclusive of any spread and is a per annum rate, expressed as a decimal. The floor rate of 5% would be represented as 0.05.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.rate_observation import RateObservation
from src.models.cdm.generated.product.template.strike import Strike
FloatingRateDefinition.model_rebuild()
