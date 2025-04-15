from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class UmbrellaAgreementEntity(CdmModelBase):
    """A class to specify the legal entities that are part of the umbrella agreement."""
    entity_id: List[ForwardRef("FieldWithMetaString")] = Field(None, description="A legal entity identifier (e.g. RED entity code).")
    name: ForwardRef("FieldWithMetaString") = Field(None, description="The legal entity name.")
    terms: str = Field(None, description="The terms that might be associated with each party to the umbrella agreement.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
UmbrellaAgreementEntity.model_rebuild()
