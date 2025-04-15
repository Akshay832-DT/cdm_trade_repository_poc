"""FIX message model for TradingSessionStatus (h).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase

class TradingSessionStatusMessage(FIXMessageBase):
    """FIX message model for TradingSessionStatus."""

    MsgType: str = Field("h", alias="35")

    TradSesReqID: Optional[str] = Field(None, alias='335', description='')
    TradingSessionID: str = Field(..., alias='336', description='')
    TradingSessionSubID: Optional[str] = Field(None, alias='625', description='')
    TradSesMethod: Optional[int] = Field(None, alias='338', description='')
    TradSesMode: Optional[int] = Field(None, alias='339', description='')
    UnsolicitedIndicator: Optional[bool] = Field(None, alias='325', description='')
    TradSesStatus: int = Field(..., alias='340', description='')
    TradSesStatusRejReason: Optional[int] = Field(None, alias='567', description='')
    TradSesStartTime: Optional[datetime] = Field(None, alias='341', description='')
    TradSesOpenTime: Optional[datetime] = Field(None, alias='342', description='')
    TradSesPreCloseTime: Optional[datetime] = Field(None, alias='343', description='')
    TradSesCloseTime: Optional[datetime] = Field(None, alias='344', description='')
    TradSesEndTime: Optional[datetime] = Field(None, alias='345', description='')
    TotalVolumeTraded: Optional[float] = Field(None, alias='387', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')

