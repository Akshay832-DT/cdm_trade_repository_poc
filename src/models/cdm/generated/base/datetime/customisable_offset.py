from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.offset import Offset

class CustomisableOffset(CdmModelBase):
    """A class to specify an offset either as a normalized [multiplier, period, dayType] or as a custom provision of type string."""
    offset: ForwardRef("Offset") = Field(None)
    custom_provision: str = Field(None)

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.offset import Offset
CustomisableOffset.model_rebuild()
