"""
FIX 4.4 AllocAckGrp Component

This module contains the Pydantic model for the AllocAckGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class NoAllocs(FIXMessageBase):
    """
    NoAllocs group fields
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
    
    allocAccount: Optional[str] = Field(None, description='', alias='79')
    allocAcctIDSource: Optional[int] = Field(None, description='', alias='661')
    allocPrice: Optional[float] = Field(None, description='', alias='366')
    individualAllocID: Optional[str] = Field(None, description='', alias='467')
    individualAllocRejCode: Optional[int] = Field(None, description='', alias='776')
    allocText: Optional[str] = Field(None, description='', alias='161')
    encodedAllocTextLen: Optional[int] = Field(None, description='', alias='360')
    encodedAllocText: Optional[str] = Field(None, description='', alias='361')


class AllocAckGrp(FIXMessageBase):
    """
    FIX 4.4 AllocAckGrp Component
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
    
    noAllocs: Optional[int] = Field(None, description='Number of NoAllocs entries', alias='78')
    noAllocs_items: List[NoAllocs] = Field(default_factory=list)
