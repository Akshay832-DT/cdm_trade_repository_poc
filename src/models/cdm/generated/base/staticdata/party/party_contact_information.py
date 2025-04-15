from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.business_unit import BusinessUnit
    from src.models.cdm.generated.base.staticdata.party.contact_information import ContactInformation
    from src.models.cdm.generated.base.staticdata.party.natural_person import NaturalPerson
    from src.models.cdm.generated.metafields.reference_with_meta_party import ReferenceWithMetaParty

class PartyContactInformation(CdmModelBase):
    """A class to specify contact information within a party: address and, optionally, associated business unit and person. This class also supports the ISDA CSA representation as a single string, through the address attribute."""
    party_reference: ForwardRef("ReferenceWithMetaParty") = Field(None, description="The reference to the party to which the contact information refers to.")
    contact_information: ForwardRef("ContactInformation") = Field(None, description="The postal/street address, telephone number, email address and/or web page. If the contact information is specific to the associated business unit(s), it should be associated with those.")
    business_unit: List[ForwardRef("BusinessUnit")] = Field(None, description="Optional organization unit information used to describe the organization units (e.g. trading desks) involved in a transaction or business process, incl. the contact information (when relevant).")
    person: List[ForwardRef("NaturalPerson")] = Field(None, description="Optional information about people involved in a transaction or business process. (These are employees of the party.)")
    additional_information: str = Field(None, description="Specification of special instructions of the relevant party.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.business_unit import BusinessUnit
from src.models.cdm.generated.base.staticdata.party.contact_information import ContactInformation
from src.models.cdm.generated.base.staticdata.party.natural_person import NaturalPerson
from src.models.cdm.generated.metafields.reference_with_meta_party import ReferenceWithMetaParty
PartyContactInformation.model_rebuild()
