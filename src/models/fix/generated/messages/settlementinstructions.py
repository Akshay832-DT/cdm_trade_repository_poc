"""FIX message model for SettlementInstructions (T).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.settlinstgrp import SettlInstGrpComponent

class SettlementInstructionsMessage(FIXMessageBase):
    """FIX message model for SettlementInstructions."""

    MsgType: str = Field("T", alias="35")

    SettlInstMsgID: str = Field(..., alias='777', description='')
    SettlInstReqID: Optional[str] = Field(None, alias='791', description='')
    SettlInstMode: str = Field(..., alias='160', description='')
    SettlInstReqRejCode: Optional[int] = Field(None, alias='792', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    ClOrdID: Optional[str] = Field(None, alias='11', description='')
    TransactTime: datetime = Field(..., alias='60', description='')
    SettlInstGrp: Optional[SettlInstGrpComponent] = Field(None, description='')

