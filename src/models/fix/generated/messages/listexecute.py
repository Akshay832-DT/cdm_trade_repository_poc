"""FIX message model for ListExecute (L).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase

class ListExecuteMessage(FIXMessageBase):
    """FIX message model for ListExecute."""

    MsgType: str = Field("L", alias="35")

    ListID: str = Field(..., alias='66', description='')
    ClientBidID: Optional[str] = Field(None, alias='391', description='')
    BidID: Optional[str] = Field(None, alias='390', description='')
    TransactTime: datetime = Field(..., alias='60', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')

