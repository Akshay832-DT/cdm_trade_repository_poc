from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.account import Account
    from src.models.cdm.generated.base.staticdata.party.business_unit import BusinessUnit
    from src.models.cdm.generated.base.staticdata.party.contact_information import ContactInformation
    from src.models.cdm.generated.base.staticdata.party.natural_person import NaturalPerson
    from src.models.cdm.generated.base.staticdata.party.natural_person_role import NaturalPersonRole
    from src.models.cdm.generated.base.staticdata.party.party_identifier import PartyIdentifier
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class Party(CdmModelBase):
    """A class to specify a party, without a qualification as to whether this party is a legal entity or a natural person, although the model provides the ability to associate a person (or set of persons) to a party, which use case would imply that such party would be a legal entity (even if not formally specified as such). """
    party_id: List[ForwardRef("PartyIdentifier")] = Field(None, description="The identifier associated with a party, e.g. the 20 digits LEI code.")
    name: ForwardRef("FieldWithMetaString") = Field(None, description="The party name.")
    business_unit: List[ForwardRef("BusinessUnit")] = Field(None, description="Optional organization unit information used to describe the organization units (e.g. trading desks) involved in a transaction or business process, incl. the contact information (when relevant).")
    person: List[ForwardRef("NaturalPerson")] = Field(None, description="The person(s) who might be associated with the party as part of the execution, contract or legal document.")
    person_role: List[ForwardRef("NaturalPersonRole")] = Field(None, description="The role of the person(s) ")
    account: ForwardRef("Account") = Field(None, description="The account that might be associated with the party. At most one account can be specified, as it is expected that this information is used in the context of a contract or legal document where only one account per party can be associated with such object.")
    contact_information: ForwardRef("ContactInformation") = Field(None, description="The postal/street address, telephone number, email address and/or web page. If the contact information is specific to the associated business unit(s) or person (s), it should be associated with those.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.account import Account
from src.models.cdm.generated.base.staticdata.party.business_unit import BusinessUnit
from src.models.cdm.generated.base.staticdata.party.contact_information import ContactInformation
from src.models.cdm.generated.base.staticdata.party.natural_person import NaturalPerson
from src.models.cdm.generated.base.staticdata.party.natural_person_role import NaturalPersonRole
from src.models.cdm.generated.base.staticdata.party.party_identifier import PartyIdentifier
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
Party.model_rebuild()
