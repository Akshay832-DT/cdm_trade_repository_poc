from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.position.inventory_record import InventoryRecord

class Inventory(CdmModelBase):
    """A data type that can be used to describe an inventory of securities."""
    inventory_record: List[ForwardRef("InventoryRecord")] = Field(None, description="An array holding the list of inventory being described. Each element in the inventoryRecord array represents an individual piece of inventory i.e. a security.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.position.inventory_record import InventoryRecord
Inventory.model_rebuild()
