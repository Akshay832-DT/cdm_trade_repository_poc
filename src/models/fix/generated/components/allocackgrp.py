"""
FIX 4.4 AllocAckGrp Component

This module contains the Pydantic model for the AllocAckGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class AllocAckGrp(TradeModel):
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
    AllocAccount: Optional[str] = Field(None, description='', alias='79')
    AllocAcctIDSource: Optional[int] = Field(None, description='', alias='661')
    AllocPrice: Optional[float] = Field(None, description='', alias='366')
    IndividualAllocID: Optional[str] = Field(None, description='', alias='467')
    IndividualAllocRejCode: Optional[int] = Field(None, description='', alias='776')
    AllocText: Optional[str] = Field(None, description='', alias='161')
    EncodedAllocTextLen: Optional[int] = Field(None, description='', alias='360')
    EncodedAllocText: Optional[str] = Field(None, description='', alias='361')


class NoAllocs(TradeModel):
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
    AllocAccount: Optional[str] = Field(None, description='', alias='79')
    AllocAcctIDSource: Optional[int] = Field(None, description='', alias='661')
    AllocPrice: Optional[float] = Field(None, description='', alias='366')
    IndividualAllocID: Optional[str] = Field(None, description='', alias='467')
    IndividualAllocRejCode: Optional[int] = Field(None, description='', alias='776')
    AllocText: Optional[str] = Field(None, description='', alias='161')
    EncodedAllocTextLen: Optional[int] = Field(None, description='', alias='360')
    EncodedAllocText: Optional[str] = Field(None, description='', alias='361')

    NoAllocss: List[NoAllocs] = Field(default_factory=list)
