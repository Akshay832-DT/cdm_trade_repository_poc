from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.rfqreqgrp import RFQReqGrpComponent

class RFQRequest(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    RFQReqID: str = Field(..., description='', alias='644')
    SubscriptionRequestType: Optional[str] = Field(None, description='', alias='263')
    RFQReqGrp: RFQReqGrpComponent = Field(..., description='RFQReqGrp component')

