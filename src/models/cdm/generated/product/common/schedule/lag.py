from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.offset import Offset

class Lag(CdmModelBase):
    """The pricing period per calculation period if the pricing days do not wholly fall within the respective calculation period."""
    lag_duration: ForwardRef("Offset") = Field(description="Defines the offset of the series of pricing dates relative to the calculation period.")
    first_observation_date_offset: ForwardRef("Offset") = Field(None, description="Defines the offset of the series of pricing dates relative to the calculation period.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.offset import Offset
Lag.model_rebuild()
