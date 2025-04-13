from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.settlinstgrp import SettlInstGrpComponent

class SettlementInstructions(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    SettlInstMsgID: str = Field(..., description='', alias='777')
    SettlInstReqID: Optional[str] = Field(None, description='', alias='791')
    SettlInstMode: str = Field(..., description='', alias='160')
    SettlInstReqRejCode: Optional[int] = Field(None, description='', alias='792')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    ClOrdID: Optional[str] = Field(None, description='', alias='11')
    TransactTime: datetime = Field(..., description='', alias='60')
    SettlInstGrp: Optional[SettlInstGrpComponent] = Field(None, description='SettlInstGrp component')

