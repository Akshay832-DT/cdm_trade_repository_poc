"""
FIX 4.4 SettlParties Component

This module contains the Pydantic model for the SettlParties component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class SettlParties(FIXMessageBase):
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
    settlPartyID: Optional[str] = Field(None, description='', alias='782')
    settlPartyIDSource: Optional[str] = Field(None, description='', alias='783')
    settlPartyRole: Optional[int] = Field(None, description='', alias='784')
    settlPtysSubGrp: Optional[str] = Field(None)


class NoSettlPartyIDs(FIXMessageBase):
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
    settlPartyID: Optional[int] = Field(None, description='', alias='781')
    settlPartyIDSource: Optional[int] = Field(None, description='', alias='781')
    settlPartyRole: Optional[int] = Field(None, description='', alias='781')

    noSettlPartyIDss: List[NoSettlPartyIDs] = Field(default_factory=list)
