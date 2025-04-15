from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class ObservationParameters(CdmModelBase):
    """Parameters on daily observed computed rates, specifically daily caps and floors. This type is used to represent modular computed rates in interestRatePayouts."""
    observation_cap_rate: float = Field(None, description="A daily observation cap rate.")
    observation_floor_rate: float = Field(None, description="A daily observation floor rate.")

# Import after class definition to avoid circular imports
ObservationParameters.model_rebuild()
