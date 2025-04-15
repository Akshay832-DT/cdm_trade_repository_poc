"""
FpML Complex Type - PartyTradeIdentifierType
"""

from typing import List, Optional, Any, Dict, ForwardRef, TYPE_CHECKING
from pydantic import Field
from datetime import date, datetime, time
from ..base import FpMLModelBase

# Import directly for use at runtime
from .party_reference_type import PartyReferenceType

# Only use the forward references for type checking
PartyReferenceTypeRef = ForwardRef('PartyReferenceType')

class PartyTradeIdentifierType(FpMLModelBase):
    class Config:
        populate_by_field_name = True
        validate_assignment = True

    partyReference: PartyReferenceType = Field()
    tradeId: str = Field()

# Update forward references
PartyTradeIdentifierType.update_forward_refs()
