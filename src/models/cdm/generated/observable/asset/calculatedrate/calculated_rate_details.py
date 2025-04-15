from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.calculatedrate.calculated_rate_observations import CalculatedRateObservations

class CalculatedRateDetails(CdmModelBase):
    """Type for reporting details of calculated rates, including the observations that went into the final reported rate."""
    observations: ForwardRef("CalculatedRateObservations") = Field(None, description="The observation dates and weights for each observation date.")
    weighted_rates: List[List] = Field(None, description="The weighted value of each observation.")
    growth_factor: List[List] = Field(None, description="The daily growth factors, showing the weighted rates divided by the day count basis plus one, giving how much the value grows for each step in the calculation.")
    compounded_growth: List[List] = Field(None, description="The compounding curve, showing how the initial value grew during the calculation period.")
    aggregate_value: float = Field(None, description="The total sum or product of all the individual terms that went into the calculated rate.")
    aggregate_weight: float = Field(None, description="The total weight of all the terms that went into the calculated rate.")
    calculated_rate: float = Field(None, description="The resulting calculated weight.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.calculatedrate.calculated_rate_observations import CalculatedRateObservations
CalculatedRateDetails.model_rebuild()
