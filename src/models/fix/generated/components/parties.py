"""
FIX 4.4 Parties Component

This module contains the Pydantic model for the Parties component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class NoPartyIDs(FIXMessageBase):
    """
    NoPartyIDs group fields
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
    
    partyID: Optional[str] = Field(None, description='', alias='448')
    partyIDSource: Optional[str] = Field(None, description='', alias='447')
    partyRole: Optional[int] = Field(None, description='', alias='452')
    # PtysSubGrp component would be added here if needed


class Parties(FIXMessageBase):
    """
    FIX 4.4 Parties Component
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
    
    noPartyIDs: Optional[int] = Field(None, description='Number of party entries', alias='453')
    noPartyIDs_items: List[NoPartyIDs] = Field(default_factory=list)
