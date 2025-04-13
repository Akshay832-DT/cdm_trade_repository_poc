from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.mdreqgrp import MDReqGrpComponent
from src.models.fix.generated.components.instrmtmdreqgrp import InstrmtMDReqGrpComponent
from src.models.fix.generated.components.trdgsesgrp import TrdgSesGrpComponent

class MarketDataRequest(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    MDReqID: str = Field(..., description='', alias='262')
    SubscriptionRequestType: str = Field(..., description='', alias='263')
    MarketDepth: int = Field(..., description='', alias='264')
    MDUpdateType: Optional[int] = Field(None, description='', alias='265')
    AggregatedBook: Optional[bool] = Field(None, description='', alias='266')
    OpenCloseSettlFlag: Optional[List[str]] = Field(None, description='', alias='286')
    Scope: Optional[List[str]] = Field(None, description='', alias='546')
    MDImplicitDelete: Optional[bool] = Field(None, description='', alias='547')
    ApplQueueAction: Optional[int] = Field(None, description='', alias='815')
    ApplQueueMax: Optional[int] = Field(None, description='', alias='812')
    MDReqGrp: MDReqGrpComponent = Field(..., description='MDReqGrp component')
    InstrmtMDReqGrp: InstrmtMDReqGrpComponent = Field(..., description='InstrmtMDReqGrp component')
    TrdgSesGrp: Optional[TrdgSesGrpComponent] = Field(None, description='TrdgSesGrp component')

