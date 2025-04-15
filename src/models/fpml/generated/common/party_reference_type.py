"""
FpML Complex Type - PartyReferenceType
"""

from typing import List, Optional, Any, Dict, ForwardRef, TYPE_CHECKING
from pydantic import Field
from datetime import date, datetime, time
from ..base import FpMLModelBase

class PartyReferenceType(FpMLModelBase):
    class Config:
        populate_by_field_name = True
        validate_assignment = True

    href: Optional[str] = Field(None, alias='@href')

# Update forward references
PartyReferenceType.update_forward_refs()
