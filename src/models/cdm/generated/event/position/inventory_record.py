from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.security import Security
    from src.models.cdm.generated.base.staticdata.identifier.assigned_identifier import AssignedIdentifier

class InventoryRecord(CdmModelBase):
    """An individual piece of inventory. This represents a single security."""
    identifer: ForwardRef("AssignedIdentifier") = Field(description="Unique identifier for this record. This can be used to uniquely identify a specific piece of inventory.")
    security: ForwardRef("Security") = Field(description="The security details.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.security import Security
from src.models.cdm.generated.base.staticdata.identifier.assigned_identifier import AssignedIdentifier
InventoryRecord.model_rebuild()
