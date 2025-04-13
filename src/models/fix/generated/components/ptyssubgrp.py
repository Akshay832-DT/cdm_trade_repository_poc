"""
FIX 4.4 PtysSubGrp Component

This module contains the Pydantic model for the PtysSubGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class NoPartySubIDs(FIXMessageBase):
    """
    NoPartySubIDs group fields
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
    
    partySubID: Optional[str] = Field(None, description='', alias='523')
    partySubIDType: Optional[int] = Field(None, description='', alias='803')


class PtysSubGrp(FIXMessageBase):
    """
    FIX 4.4 PtysSubGrp Component
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
    
    noPartySubIDs: Optional[int] = Field(None, description='Number of NoPartySubIDs entries', alias='802')
    noPartySubIDs_items: List[NoPartySubIDs] = Field(default_factory=list)
