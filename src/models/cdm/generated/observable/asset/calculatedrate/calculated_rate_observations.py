from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CalculatedRateObservations(CdmModelBase):
    """Type for reporting observations that went into the final reported rate."""
    observation_dates: List[List] = Field(None, description="The observation date upon which the rate is observed.")
    weights: List[List] = Field(None, description="The corresponding weight for each date.")
    observed_rates: List[List] = Field(None, description="The value observed for that date")
    processed_rates: List[List] = Field(None, description="The value after any processing, such as application of caps or floors.")

# Import after class definition to avoid circular imports
CalculatedRateObservations.model_rebuild()
