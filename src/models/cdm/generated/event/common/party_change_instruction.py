from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

# Import dependencies first
from src.models.cdm.generated.base.staticdata.party.ancillary_party import AncillaryParty
from src.models.cdm.generated.base.staticdata.party.counterparty import Counterparty
from src.models.cdm.generated.base.staticdata.party.party_role import PartyRole
from src.models.cdm.generated.event.common.trade_identifier import TradeIdentifier

# Ensure dependencies are rebuilt first
AncillaryParty.model_rebuild()
Counterparty.model_rebuild()
PartyRole.model_rebuild()
TradeIdentifier.model_rebuild()

class PartyChangeInstruction(CdmModelBase):
    """Specifies instruction to change the party on a trade. This primitive instruction is used in a number of scenarios including: clearing, allocation and novation. The instrution must include a trade identifier, because a change of party effectively results in a different trade."""
    counterparty: "Counterparty" = Field(description="The new counterparty who is stepping into the trade. The stepping out counterparty is inferred based on the counterparty role that is being updated.")
    ancillary_party: Optional["AncillaryParty"] = Field(None, description="Specifies an ancillary party to be added onto the new transaction, e.g. the original executing party in an allocation.")
    party_role: Optional["PartyRole"] = Field(None, description="Specifies an additional party roles to be added on to the new transaction.")
    trade_id: Optional[List["TradeIdentifier"]] = Field(None, description="The identifier to be assigned to the new trade post change of party.")

# Rebuild this model after its definition
PartyChangeInstruction.model_rebuild()
