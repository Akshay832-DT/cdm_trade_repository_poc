from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.common.schedule.weighted_averaging_observation import WeightedAveragingObservation

class AveragingObservationList(CdmModelBase):
    """An unordered list of weighted averaging observations."""
    averaging_observation: List[ForwardRef("WeightedAveragingObservation")] = Field(None, description="A single weighted averaging observation.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.common.schedule.weighted_averaging_observation import WeightedAveragingObservation
AveragingObservationList.model_rebuild()
