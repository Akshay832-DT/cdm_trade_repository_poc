"""
FpML Complex Type - TradeHeaderType
"""

from typing import List, Optional, Any, Dict, ForwardRef, TYPE_CHECKING
from pydantic import Field
from datetime import date, datetime, time
from ..base import FpMLModelBase

# Import directly for use at runtime
from .party_trade_identifier_type import PartyTradeIdentifierType

# Only use the forward references for type checking
PartyTradeIdentifierTypeRef = ForwardRef('PartyTradeIdentifierType')

class TradeHeaderType(FpMLModelBase):
    class Config:
        populate_by_field_name = True
        validate_assignment = True

    partyTradeIdentifier: List[PartyTradeIdentifierType] = Field()
    tradeDate: date = Field()
    clearedDate: Optional[date] = Field(None)

# Update forward references
TradeHeaderType.update_forward_refs()
