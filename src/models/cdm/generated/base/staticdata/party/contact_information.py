from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.address import Address
    from src.models.cdm.generated.base.staticdata.party.telephone_number import TelephoneNumber

class ContactInformation(CdmModelBase):
    """A class to specify contact information associated with a party: telephone, postal/street address, email and web page."""
    telephone: List[ForwardRef("TelephoneNumber")] = Field(None, description="The telephone number.")
    address: List[ForwardRef("Address")] = Field(None, description="The street/postal address.")
    email: List[List] = Field(None, description="The email address.")
    web_page: List[List] = Field(None, description="The web page. This attribute is not specified as part of the FpML ContactInformation complex type.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.address import Address
from src.models.cdm.generated.base.staticdata.party.telephone_number import TelephoneNumber
ContactInformation.model_rebuild()
