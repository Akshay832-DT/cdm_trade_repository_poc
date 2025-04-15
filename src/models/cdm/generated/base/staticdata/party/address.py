from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class Address(CdmModelBase):
    """A class to specify a post or street address."""
    street: List[List] = Field(None, description="The set of street and building number information that identifies a postal address within a city.")
    city: str = Field(None, description="The city component of the postal address.")
    state: str = Field(None, description="A country subdivision used in postal addresses in some countries. For example, US states, Canadian provinces, Swiss cantons, ...")
    country: ForwardRef("FieldWithMetaString") = Field(None, description="The ISO 3166 standard code for the country within which the postal address is located.")
    postal_code: str = Field(None, description="The code, required for computerized mail sorting systems, that is allocated to a physical address by a national postal authority.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
Address.model_rebuild()
