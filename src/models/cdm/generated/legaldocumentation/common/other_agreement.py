from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class OtherAgreement(CdmModelBase):
    """A class for defining an agreement executed between parties."""
    identifier: ForwardRef("FieldWithMetaString") = Field(None, description="An identifier that has been created to identify the agreement.")
    other_agreement_type: ForwardRef("FieldWithMetaString") = Field(description="The agreement executed between the parties and intended to govern product-specific derivatives transactions between those parties.")
    version: ForwardRef("FieldWithMetaString") = Field(None, description="The version of the agreement.")
    date: str = Field(None, description="The date on which the agreement was signed.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
OtherAgreement.model_rebuild()
