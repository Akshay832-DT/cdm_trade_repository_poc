from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class ListingSector(CdmModelBase):
    """Specifies a filter based on an industry sector."""
    sector: List[ForwardRef("FieldWithMetaString")] = Field(None, description="Represents a filter based on an industry sector defined under a system for classifying industry types such as Global Industry Classification Standard (GICS) and North American Industry Classification System (NAICS)")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
ListingSector.model_rebuild()
