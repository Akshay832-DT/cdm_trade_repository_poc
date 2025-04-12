"""
FIX 4.4 SettlParties Component

This module contains the Pydantic model for the SettlParties component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class SettlParties(TradeModel):
    """
    FIX 4.4 SettlParties Component
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
    SettlPartyID: Optional[str] = Field(None, description='', alias='782')
    SettlPartyIDSource: Optional[str] = Field(None, description='', alias='783')
    SettlPartyRole: Optional[int] = Field(None, description='', alias='784')
    SettlPtysSubGrp: Optional[str] = Field(None)


class NoSettlPartyIDs(TradeModel):
    """
    NoSettlPartyIDs group fields
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
    SettlPartyID: Optional[str] = Field(None, description='', alias='782')
    SettlPartyIDSource: Optional[str] = Field(None, description='', alias='783')
    SettlPartyRole: Optional[int] = Field(None, description='', alias='784')

    NoSettlPartyIDss: List[NoSettlPartyIDs] = Field(default_factory=list)
