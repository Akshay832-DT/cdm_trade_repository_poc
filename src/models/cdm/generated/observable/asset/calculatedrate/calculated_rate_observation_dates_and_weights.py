from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CalculatedRateObservationDatesAndWeights(CdmModelBase):
    """Type for reporting the observations dates and the corresponding weights going into a daily calculated rate"""
    observation_dates: List[List] = Field(None, description="The observation date upon which the rate is observed.")
    weights: List[List] = Field(None, description="The corresponding weight for each date.")

# Import after class definition to avoid circular imports
CalculatedRateObservationDatesAndWeights.model_rebuild()
