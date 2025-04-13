"""
FIX 4.4 NstdPtys2SubGrp Component

This module contains the Pydantic model for the NstdPtys2SubGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class NoNested2PartySubIDs(FIXMessageBase):
    """
    NoNested2PartySubIDs group fields
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
    
    nested2PartySubID: Optional[str] = Field(None, description='', alias='760')
    nested2PartySubIDType: Optional[int] = Field(None, description='', alias='807')


class NstdPtys2SubGrp(FIXMessageBase):
    """
    FIX 4.4 NstdPtys2SubGrp Component
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
    
    noNested2PartySubIDs: Optional[int] = Field(None, description='Number of NoNested2PartySubIDs entries', alias='806')
    noNested2PartySubIDs_items: List[NoNested2PartySubIDs] = Field(default_factory=list)
