from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.parties import PartiesComponent
from src.models.fix.generated.components.allocackgrp import AllocAckGrpComponent

class AllocationInstructionAck(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    AllocID: str = Field(..., description='', alias='70')
    SecondaryAllocID: Optional[str] = Field(None, description='', alias='793')
    TradeDate: Optional[date] = Field(None, description='', alias='75')
    TransactTime: datetime = Field(..., description='', alias='60')
    AllocStatus: int = Field(..., description='', alias='87')
    AllocRejCode: Optional[int] = Field(None, description='', alias='88')
    AllocType: Optional[int] = Field(None, description='', alias='626')
    AllocIntermedReqType: Optional[int] = Field(None, description='', alias='808')
    MatchStatus: Optional[str] = Field(None, description='', alias='573')
    Product: Optional[int] = Field(None, description='', alias='460')
    SecurityType: Optional[str] = Field(None, description='', alias='167')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    Parties: Optional[PartiesComponent] = Field(None, description='Parties component')
    AllocAckGrp: Optional[AllocAckGrpComponent] = Field(None, description='AllocAckGrp component')

