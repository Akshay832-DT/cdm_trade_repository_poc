from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.time_zone import TimeZone
    from src.models.cdm.generated.observable.asset.information_source import InformationSource
    from src.models.cdm.generated.observable.asset.observable import Observable
    from src.models.cdm.generated.observable.event.determination_methodology import DeterminationMethodology

class ObservationIdentifier(CdmModelBase):
    """Defines the parameters needed to uniquely identify a piece of data among the population of all available market data."""
    observable: ForwardRef("Observable") = Field(description="Represents the asset or rate to which the observation relates.")
    observation_date: str = Field(description="Specifies the date value to use when resolving the market data.")
    observation_time: ForwardRef("TimeZone") = Field(None, description="Represents the time and time-zone.")
    information_source: ForwardRef("InformationSource") = Field(None, description="Represents where the market data published and should be observed.")
    determination_methodology: ForwardRef("DeterminationMethodology") = Field(None, description="Specifies the method according to which an amount or a date is determined.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.time_zone import TimeZone
from src.models.cdm.generated.observable.asset.information_source import InformationSource
from src.models.cdm.generated.observable.asset.observable import Observable
from src.models.cdm.generated.observable.event.determination_methodology import DeterminationMethodology
ObservationIdentifier.model_rebuild()
