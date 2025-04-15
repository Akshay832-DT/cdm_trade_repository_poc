from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.party_contact_information import PartyContactInformation
    from src.models.cdm.generated.product.collateral.contact_election import ContactElection

class AddressForNotices(CdmModelBase):
    """Specification of the address and other details for notices."""
    primary_notices: ForwardRef("ContactElection") = Field(description="Specification of primary notice details")
    additional_notices: List[ForwardRef("PartyContactInformation")] = Field(None, description="The optional specification of additional information when a party requires notices to be delivered to more than one address.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.party_contact_information import PartyContactInformation
from src.models.cdm.generated.product.collateral.contact_election import ContactElection
AddressForNotices.model_rebuild()
