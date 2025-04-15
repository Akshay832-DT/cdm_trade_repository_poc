from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class MarginTypeEnum(CdmModelBase):
    """This indicator defines which type of assets (cash or securities) is specified to apply as margin to the repo transaction."""
    # Enum values
    Cash: ClassVar[str] = "Cash"
    Instrument: ClassVar[str] = "Instrument"


# Import after class definition to avoid circular imports
MarginTypeEnum.model_rebuild()
