from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.contact_information import ContactInformation
    from src.models.cdm.generated.metafields.field_with_meta_person_identifier import FieldWithMetaPersonIdentifier

class NaturalPerson(CdmModelBase):
    """A class to represent the attributes that are specific to a natural person."""
    person_id: List[ForwardRef("FieldWithMetaPersonIdentifier")] = Field(None, description="The identifier associated with a person, e.g. the internal identification code.")
    honorific: str = Field(None, description="An honorific title, such as Mr., Ms., Dr. etc.")
    first_name: str = Field(None, description="The natural person's first name. It is optional in FpML.")
    middle_name: List[List] = Field(None, description="The natural person's middle name(s). If a middle name is provided then an initial should be absent.")
    initial: List[List] = Field(None, description="The natural person's middle initial(s). If a middle initial is provided then a name should be absent.")
    surname: str = Field(None, description="The natural person's surname.")
    suffix: str = Field(None, description="Name suffix, such as Jr., III, etc.")
    date_of_birth: str = Field(None, description="The natural person's date of birth.")
    contact_information: ForwardRef("ContactInformation") = Field(None, description="The contact information for such person, when different from the contact information associated with the party.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.contact_information import ContactInformation
from src.models.cdm.generated.metafields.field_with_meta_person_identifier import FieldWithMetaPersonIdentifier
NaturalPerson.model_rebuild()
