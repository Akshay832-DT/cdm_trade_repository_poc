"""
FIX 4.4 NestedParties2 Component

This module contains the Pydantic model for the NestedParties2 component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class NestedParties2(TradeModel):
    """
    FIX 4.4 NestedParties2 Component
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
    Nested2PartyID: Optional[str] = Field(None, description='', alias='757')
    Nested2PartyIDSource: Optional[str] = Field(None, description='', alias='758')
    Nested2PartyRole: Optional[int] = Field(None, description='', alias='759')
    NstdPtys2SubGrp: Optional[str] = Field(None)


class NoNested2PartyIDs(TradeModel):
    """
    NoNested2PartyIDs group fields
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
    Nested2PartyID: Optional[str] = Field(None, description='', alias='757')
    Nested2PartyIDSource: Optional[str] = Field(None, description='', alias='758')
    Nested2PartyRole: Optional[int] = Field(None, description='', alias='759')

    NoNested2PartyIDss: List[NoNested2PartyIDs] = Field(default_factory=list)
