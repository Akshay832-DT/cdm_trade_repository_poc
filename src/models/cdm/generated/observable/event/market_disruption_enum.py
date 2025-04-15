from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class MarketDisruptionEnum(CdmModelBase):
    """The enumerated values to specify the handling of an averaging date market disruption for an equity derivative transaction."""
    # Enum values
    ModifiedPostponement: ClassVar[str] = "ModifiedPostponement"
    Omission: ClassVar[str] = "Omission"
    Postponement: ClassVar[str] = "Postponement"


# Import after class definition to avoid circular imports
MarketDisruptionEnum.model_rebuild()
