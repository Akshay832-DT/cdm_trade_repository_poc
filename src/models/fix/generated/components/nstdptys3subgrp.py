"""
FIX 4.4 NstdPtys3SubGrp Component

This module contains the Pydantic model for the NstdPtys3SubGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoNested3PartySubIDsGroup(FIXComponentBase):
    """
    NoNested3PartySubIDs group fields
    """
    model_config = ConfigDict(
        populate_by_name=True,
        validate_by_name=True,
        json_encoders={
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
            time: lambda v: v.isoformat()
        }
    )
    
    Nested3PartySubID: Optional[str] = Field(None, description='', alias='953')
    Nested3PartySubIDType: Optional[int] = Field(None, description='', alias='954')


class NstdPtys3SubGrpComponent(FIXComponentBase):
    """
    FIX 4.4 NstdPtys3SubGrp Component
    """
    model_config = ConfigDict(
        populate_by_name=True,
        validate_by_name=True,
        json_encoders={
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
            time: lambda v: v.isoformat()
        }
    )
    
    NoNested3PartySubIDs: Optional[int] = Field(None, description='Number of NoNested3PartySubIDs entries', alias='')
    NoNested3PartySubIDs_items: List[NoNested3PartySubIDsGroup] = Field(default_factory=list)
