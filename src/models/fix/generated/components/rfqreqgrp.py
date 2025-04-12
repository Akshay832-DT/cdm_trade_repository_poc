"""
FIX 4.4 RFQReqGrp Component

This module contains the Pydantic model for the RFQReqGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class RFQReqGrp(FIXMessageBase):
    """
    FIX 4.4 RFQReqGrp Component
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
    prevClosePx: Optional[float] = Field(None, description='', alias='140')
    quoteRequestType: Optional[int] = Field(None, description='', alias='303')
    quoteType: Optional[int] = Field(None, description='', alias='537')
    tradingSessionID: Optional[str] = Field(None, description='', alias='336')
    tradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    instrument: str = Field(None)
    undInstrmtGrp: Optional[str] = Field(None)
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
    prevClosePx: Optional[int] = Field(None, description='', alias='146')
    quoteRequestType: Optional[int] = Field(None, description='', alias='146')
    quoteType: Optional[int] = Field(None, description='', alias='146')
    tradingSessionID: Optional[int] = Field(None, description='', alias='146')
    tradingSessionSubID: Optional[int] = Field(None, description='', alias='146')

    noRelatedSyms: List[NoRelatedSym] = Field(default_factory=list)
