from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.party import Party
    from src.models.cdm.generated.base.staticdata.party.party_role import PartyRole
    from src.models.cdm.generated.event.position.available_inventory_record import AvailableInventoryRecord
    from src.models.cdm.generated.event.position.available_inventory_type_enum import AvailableInventoryTypeEnum
    from src.models.cdm.generated.event.workflow.message_information import MessageInformation

class AvailableInventory(CdmModelBase):
    """A data type that can be used to describe the inventory of securities that a party holds. The securities are held in the AvailableInventoryRecord, with each item in the array being an individual security and its associated criteria. Criteria can include the quantity available, the rate at which the security is available to borrow at, as well as other details that can affect the decision as to whether a party wants to utilise the securities listed."""
    available_inventory_type: ForwardRef("AvailableInventoryTypeEnum") = Field(description="Defines the purpose of this inventory.")
    message_information: ForwardRef("MessageInformation") = Field(None, description="Allows details related to the availability messaging use case to be defined")
    party: List[ForwardRef("Party")] = Field(None, description="Defines all parties involved for the list of inventory records in this set of inventory. For example, when used to describe securities lending availability, this could hold the sender of the availability, the intended recipient, the beneficial owner(s), the lender (which may differ from the sender as the lender may have the same piece of availability going through multiple agents), an agent or a venue.")
    party_role: List[ForwardRef("PartyRole")] = Field(None, description="Defines the role(s) that party(ies) may have in relation to the inventory.")
    available_inventory_record: List[ForwardRef("AvailableInventoryRecord")] = Field(None, description="An array holding the list of inventory being described. Each element in the inventoryRecord array represents an individual piece of inventory i.e. a security.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.party import Party
from src.models.cdm.generated.base.staticdata.party.party_role import PartyRole
from src.models.cdm.generated.event.position.available_inventory_record import AvailableInventoryRecord
from src.models.cdm.generated.event.position.available_inventory_type_enum import AvailableInventoryTypeEnum
from src.models.cdm.generated.event.workflow.message_information import MessageInformation
AvailableInventory.model_rebuild()
