from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.party import Party
    from src.models.cdm.generated.event.common.trade_state import TradeState

class ClearingInstruction(CdmModelBase):
    """All information required to perform the clear life cycle event; the clearing party (CCP), the two parties facing each other on the alpha contract, and optionally the parties acting as clearing members."""
    alpha_contract: ForwardRef("TradeState") = Field(description="The contract that will be submitted to the clearing house for clearing. The contract should indicate that it should be cleared by assigning a clearing organisation as a party role.")
    clearing_party: ForwardRef("Party") = Field(description="The Central Counter party (CCP) that the contract will be submitted to for clearing.")
    party1: ForwardRef("Party") = Field(description="First party facing the CCP if it is clearing for its own account.")
    party2: ForwardRef("Party") = Field(description="Second party facing the CCP if it is clearing for its own account.")
    clearer_party1: ForwardRef("Party") = Field(None, description="Optional party facing the CCP, acting as clearing member for party1.")
    clearer_party2: ForwardRef("Party") = Field(None, description="Optional party facing the CCP, acting as clearing member for party2.")
    is_open_offer: bool = Field(None, description="Open Offer")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.party import Party
from src.models.cdm.generated.event.common.trade_state import TradeState
ClearingInstruction.model_rebuild()
