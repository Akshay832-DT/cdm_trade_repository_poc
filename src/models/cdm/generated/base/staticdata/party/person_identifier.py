from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.person_identifier_type_enum import PersonIdentifierTypeEnum
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class PersonIdentifier(CdmModelBase):
    """Comprises an identifier and a source. The associated metadata key denotes the ability to associate a hash value to the PersonIdentifier instantiations for the purpose of model cross-referencing, in support of functionality such as the event effect and the lineage."""
    identifier: ForwardRef("FieldWithMetaString") = Field(description="Provides an identifier associated with a person. The identifier is unique within the public source specified in the source attribute.")
    identifier_type: ForwardRef("PersonIdentifierTypeEnum") = Field(None, description="Defines the source of the identifier.")
    country: ForwardRef("FieldWithMetaString") = Field(None, description="The ISO 3166 standard code for the country issuing the identifier.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.person_identifier_type_enum import PersonIdentifierTypeEnum
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
PersonIdentifier.model_rebuild()
