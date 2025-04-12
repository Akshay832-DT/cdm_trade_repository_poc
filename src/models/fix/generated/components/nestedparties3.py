"""
FIX 4.4 NestedParties3 Component

This module contains the Pydantic model for the NestedParties3 component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class NestedParties3(TradeModel):
    """
    FIX 4.4 NestedParties3 Component
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
    Nested3PartyID: Optional[str] = Field(None, description='', alias='949')
    Nested3PartyIDSource: Optional[str] = Field(None, description='', alias='950')
    Nested3PartyRole: Optional[int] = Field(None, description='', alias='951')
    NstdPtys3SubGrp: Optional[str] = Field(None)


class NoNested3PartyIDs(TradeModel):
    """
    NoNested3PartyIDs group fields
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
    Nested3PartyID: Optional[str] = Field(None, description='', alias='949')
    Nested3PartyIDSource: Optional[str] = Field(None, description='', alias='950')
    Nested3PartyRole: Optional[int] = Field(None, description='', alias='951')

    NoNested3PartyIDss: List[NoNested3PartyIDs] = Field(default_factory=list)
