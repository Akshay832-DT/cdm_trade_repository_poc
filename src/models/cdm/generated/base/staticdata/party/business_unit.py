from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.identifier.identifier import Identifier
    from src.models.cdm.generated.base.staticdata.party.contact_information import ContactInformation

class BusinessUnit(CdmModelBase):
    """A class to specify an organizational unit."""
    name: str = Field(description="A name used to describe the organizational unit")
    identifier: ForwardRef("Identifier") = Field(None, description="An identifier used to uniquely identify the organizational unit")
    contact_information: ForwardRef("ContactInformation") = Field(None, description="The contact information for such business unit, when different from the contact information associated with the party.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.identifier.identifier import Identifier
from src.models.cdm.generated.base.staticdata.party.contact_information import ContactInformation
BusinessUnit.model_rebuild()
