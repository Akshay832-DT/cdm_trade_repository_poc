"""FIX message model for SecurityTypeRequest (v).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase

class SecurityTypeRequestMessage(FIXMessageBase):
    """FIX message model for SecurityTypeRequest."""

    MsgType: str = Field("v", alias="35")

    SecurityReqID: str = Field(..., alias='320', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    TradingSessionID: Optional[str] = Field(None, alias='336', description='')
    TradingSessionSubID: Optional[str] = Field(None, alias='625', description='')
    Product: Optional[int] = Field(None, alias='460', description='')
    SecurityType: Optional[str] = Field(None, alias='167', description='')
    SecuritySubType: Optional[str] = Field(None, alias='762', description='')

