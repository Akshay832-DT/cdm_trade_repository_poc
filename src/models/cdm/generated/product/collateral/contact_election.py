from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.party_contact_information import PartyContactInformation

class ContactElection(CdmModelBase):
    """A class to specify the parties' election to specify contact information, in relation to elections such as the Addresses for Transfer or the Demand and Notices as specified in the ISDA Credit Support Annex agreement."""
    party_election: List[ForwardRef("PartyContactInformation")] = Field(None, description="The parties' contact information election.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.party_contact_information import PartyContactInformation
ContactElection.model_rebuild()
