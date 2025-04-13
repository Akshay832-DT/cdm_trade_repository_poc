from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.quotreqrjctgrp import QuotReqRjctGrpComponent

class QuoteRequestReject(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    QuoteReqID: str = Field(..., description='', alias='131')
    RFQReqID: Optional[str] = Field(None, description='', alias='644')
    QuoteRequestRejectReason: int = Field(..., description='', alias='658')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    QuotReqRjctGrp: QuotReqRjctGrpComponent = Field(..., description='QuotReqRjctGrp component')

