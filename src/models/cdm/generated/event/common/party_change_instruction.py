from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.ancillary_party import AncillaryParty
    from src.models.cdm.generated.base.staticdata.party.counterparty import Counterparty
    from src.models.cdm.generated.base.staticdata.party.party_role import PartyRole
    from src.models.cdm.generated.event.common.trade_identifier import TradeIdentifier

class PartyChangeInstruction(CdmModelBase):
    """Specifies instruction to change the party on a trade. This primitive instruction is used in a number of scenarios including: clearing, allocation and novation. The instrution must include a trade identifier, because a change of party effectively results in a different trade."""
    counterparty: ForwardRef("Counterparty") = Field(description="The new counterparty who is stepping into the trade. The stepping out counterparty is inferred based on the counterparty role that is being updated.")
    ancillary_party: ForwardRef("AncillaryParty") = Field(None, description="Specifies an ancillary party to be added onto the new transaction, e.g. the original executing party in an allocation.")
    party_role: ForwardRef("PartyRole") = Field(None, description="Specifies an additional party roles to be added on to the new transaction.")
    trade_id: List[ForwardRef("TradeIdentifier")] = Field(None, description="The identifier to be assigned to the new trade post change of party.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.ancillary_party import AncillaryParty
from src.models.cdm.generated.base.staticdata.party.counterparty import Counterparty
from src.models.cdm.generated.base.staticdata.party.party_role import PartyRole
from src.models.cdm.generated.event.common.trade_identifier import TradeIdentifier
PartyChangeInstruction.model_rebuild()
