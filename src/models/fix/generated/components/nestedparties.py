"""
FIX 4.4 NestedParties Component

This module contains the Pydantic model for the NestedParties component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class NestedParties(TradeModel):
    """
    FIX 4.4 NestedParties Component
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
    NestedPartyID: Optional[str] = Field(None, description='', alias='524')
    NestedPartyIDSource: Optional[str] = Field(None, description='', alias='525')
    NestedPartyRole: Optional[int] = Field(None, description='', alias='538')
    NstdPtysSubGrp: Optional[str] = Field(None)


class NoNestedPartyIDs(TradeModel):
    """
    NoNestedPartyIDs group fields
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
    NestedPartyID: Optional[str] = Field(None, description='', alias='524')
    NestedPartyIDSource: Optional[str] = Field(None, description='', alias='525')
    NestedPartyRole: Optional[int] = Field(None, description='', alias='538')

    NoNestedPartyIDss: List[NoNestedPartyIDs] = Field(default_factory=list)
