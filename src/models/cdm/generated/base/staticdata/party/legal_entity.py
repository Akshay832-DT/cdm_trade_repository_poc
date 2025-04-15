from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class LegalEntity(CdmModelBase):
    """A class to specify a legal entity, with a required name and an optional entity identifier (such as the LEI)."""
    entity_id: List[ForwardRef("FieldWithMetaString")] = Field(None, description="A legal entity identifier (e.g. RED entity code).")
    name: ForwardRef("FieldWithMetaString") = Field(description="The legal entity name.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
LegalEntity.model_rebuild()
