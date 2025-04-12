"""
FIX 4.4 RFQReqGrp Component

This module contains the Pydantic model for the RFQReqGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class RFQReqGrp(TradeModel):
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
    PrevClosePx: Optional[float] = Field(None, description='', alias='140')
    QuoteRequestType: Optional[int] = Field(None, description='', alias='303')
    QuoteType: Optional[int] = Field(None, description='', alias='537')
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    Instrument: str = Field(None)
    UndInstrmtGrp: Optional[str] = Field(None)
    InstrmtLegGrp: Optional[str] = Field(None)


class NoRelatedSym(TradeModel):
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
    PrevClosePx: Optional[float] = Field(None, description='', alias='140')
    QuoteRequestType: Optional[int] = Field(None, description='', alias='303')
    QuoteType: Optional[int] = Field(None, description='', alias='537')
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')

    NoRelatedSyms: List[NoRelatedSym] = Field(default_factory=list)
