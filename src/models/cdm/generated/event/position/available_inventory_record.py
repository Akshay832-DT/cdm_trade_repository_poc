from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.math.quantity import Quantity
    from src.models.cdm.generated.base.staticdata.asset.common.security import Security
    from src.models.cdm.generated.base.staticdata.identifier.assigned_identifier import AssignedIdentifier
    from src.models.cdm.generated.base.staticdata.party.party_role import PartyRole
    from src.models.cdm.generated.observable.asset.price import Price
    from src.models.cdm.generated.product.collateral.collateral_provisions import CollateralProvisions

class AvailableInventoryRecord(CdmModelBase):
    """An individual piece of available inventory. This represents a single security and its associated criteria. The criteria are used to describe any restrictions on the securities."""
    identifer: ForwardRef("AssignedIdentifier") = Field(None, description="Unique identifier for this record. This can be used to uniquely identify a specific piece of inventory.")
    security: ForwardRef("Security") = Field(None, description="The security details.")
    expiration_date_time: str = Field(None, description="There may be a set period/time restriction associated to the security.")
    collateral: List[ForwardRef("CollateralProvisions")] = Field(None, description="The type of collateral can often be required when determining if the piece of availability being described is suitable for a party.")
    party_role: List[ForwardRef("PartyRole")] = Field(None, description="An individual security may be held by several agents. Including the party role at this level allows us to reference the party holding this specific item.")
    quantity: ForwardRef("Quantity") = Field(None, description="The quantity of the security")
    interest_rate: ForwardRef("Price") = Field(None, description="An optional element which can be used to hold a rate associated to this piece of availability.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.math.quantity import Quantity
from src.models.cdm.generated.base.staticdata.asset.common.security import Security
from src.models.cdm.generated.base.staticdata.identifier.assigned_identifier import AssignedIdentifier
from src.models.cdm.generated.base.staticdata.party.party_role import PartyRole
from src.models.cdm.generated.observable.asset.price import Price
from src.models.cdm.generated.product.collateral.collateral_provisions import CollateralProvisions
AvailableInventoryRecord.model_rebuild()
