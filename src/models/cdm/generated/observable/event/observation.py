from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.price import Price
    from src.models.cdm.generated.observable.event.observation_identifier import ObservationIdentifier

class Observation(CdmModelBase):
    """Defines a single, numerical value that was observed in the marketplace. Observations of market data are made independently to business events or trade life-cycle events, so data instances of Observation can be created independently of any other model type, hence it is annotated as a root type. Observations will be broadly reused in many situations, so references to Observation are supported via the 'key' annotation."""
    observed_value: ForwardRef("Price") = Field(description="Specifies the observed value as a number.")
    observation_identifier: ForwardRef("ObservationIdentifier") = Field(description="Represents the observation was made i.e. how to uniquely identify the observed value among the population of all available market data.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.price import Price
from src.models.cdm.generated.observable.event.observation_identifier import ObservationIdentifier
Observation.model_rebuild()
