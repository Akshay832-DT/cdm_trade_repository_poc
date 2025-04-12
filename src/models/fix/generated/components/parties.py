"""
FIX 4.4 Parties Component

This module contains the Pydantic model for the Parties component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class Parties(TradeModel):
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
    PartyID: Optional[str] = Field(None, description='', alias='448')
    PartyIDSource: Optional[str] = Field(None, description='', alias='447')
    PartyRole: Optional[int] = Field(None, description='', alias='452')
    PtysSubGrp: Optional[str] = Field(None)


class NoPartyIDs(TradeModel):
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
    PartyID: Optional[str] = Field(None, description='', alias='448')
    PartyIDSource: Optional[str] = Field(None, description='', alias='447')
    PartyRole: Optional[int] = Field(None, description='', alias='452')

    NoPartyIDss: List[NoPartyIDs] = Field(default_factory=list)
