from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.legaldocumentation.common.length_unit_enum import LengthUnitEnum

class ResourceLength(CdmModelBase):
    """A class to indicate the length of the resource."""
    length_unit: ForwardRef("LengthUnitEnum") = Field(description="The length unit of the resource. For example, pages (pdf, text documents) or time (audio, video files).")
    length_value: float = Field(description="The length value of the resource.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.legaldocumentation.common.length_unit_enum import LengthUnitEnum
ResourceLength.model_rebuild()
