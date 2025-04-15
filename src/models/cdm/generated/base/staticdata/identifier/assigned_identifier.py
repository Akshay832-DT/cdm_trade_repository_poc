from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class AssignedIdentifier(CdmModelBase):
    """A class to specify the identifier value and its associated version."""
    identifier: ForwardRef("FieldWithMetaString") = Field(description="The identifier value.")
    version: int = Field(None, description="The identifier version, which is specified as an integer and is meant to be incremented each time the transaction terms (whether contract or event) change. This version is made option to support the use case where the identifier is referenced without the version. The constraint that a contract and a lifecycle event need to have an associated version is enforced through data rules.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
AssignedIdentifier.model_rebuild()
