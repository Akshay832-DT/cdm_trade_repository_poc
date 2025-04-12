"""
FIX 4.4 RelSymDerivSecGrp Component

This module contains the Pydantic model for the RelSymDerivSecGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class RelSymDerivSecGrp(FIXMessageBase):
    """
    FIX 4.4 RelSymDerivSecGrp Component
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
    currency: Optional[str] = Field(None, description='', alias='15')
    expirationCycle: Optional[int] = Field(None, description='', alias='827')
    tradingSessionID: Optional[str] = Field(None, description='', alias='336')
    tradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')
    instrument: Optional[str] = Field(None)
    instrumentExtension: Optional[str] = Field(None)
    instrmtLegGrp: Optional[str] = Field(None)


class NoRelatedSym(FIXMessageBase):
    """
    NoRelatedSym group fields
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
    currency: Optional[int] = Field(None, description='', alias='146')
    expirationCycle: Optional[int] = Field(None, description='', alias='146')
    tradingSessionID: Optional[int] = Field(None, description='', alias='146')
    tradingSessionSubID: Optional[int] = Field(None, description='', alias='146')
    text: Optional[int] = Field(None, description='', alias='146')
    encodedTextLen: Optional[int] = Field(None, description='', alias='146')
    encodedText: Optional[int] = Field(None, description='', alias='146')

    noRelatedSyms: List[NoRelatedSym] = Field(default_factory=list)
