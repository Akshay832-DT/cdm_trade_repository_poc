from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class ObservationDate(CdmModelBase):
    """Specifies a single date on which market observations take place and specifies optional associated weighting."""
    unadjusted_date: str = Field(None, description="A date subject to adjustment.")
    adjusted_date: str = Field(None, description="The date once the adjustment has been performed. (Note that this date may change if the business center holidays change).")
    weight: float = Field(None, description="Specifies the degree of importance of the observation.")
    observation_reference: str = Field(None, description="Specifies an identification key for the market observation. This attribute can be used as a reference to assign weights to a series of dates defined in a parametricSchedule.")

# Import after class definition to avoid circular imports
ObservationDate.model_rebuild()
