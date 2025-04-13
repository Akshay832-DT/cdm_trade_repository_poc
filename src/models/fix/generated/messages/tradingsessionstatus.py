from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase

class TradingSessionStatus(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    TradSesReqID: Optional[str] = Field(None, description='', alias='335')
    TradingSessionID: str = Field(..., description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    TradSesMethod: Optional[int] = Field(None, description='', alias='338')
    TradSesMode: Optional[int] = Field(None, description='', alias='339')
    UnsolicitedIndicator: Optional[bool] = Field(None, description='', alias='325')
    TradSesStatus: int = Field(..., description='', alias='340')
    TradSesStatusRejReason: Optional[int] = Field(None, description='', alias='567')
    TradSesStartTime: Optional[datetime] = Field(None, description='', alias='341')
    TradSesOpenTime: Optional[datetime] = Field(None, description='', alias='342')
    TradSesPreCloseTime: Optional[datetime] = Field(None, description='', alias='343')
    TradSesCloseTime: Optional[datetime] = Field(None, description='', alias='344')
    TradSesEndTime: Optional[datetime] = Field(None, description='', alias='345')
    TotalVolumeTraded: Optional[float] = Field(None, description='', alias='387')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')

