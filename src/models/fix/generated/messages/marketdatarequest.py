from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.mdreqgrp import MDReqGrp
from src.models.fix.generated.components.instrmtmdreqgrp import InstrmtMDReqGrp
from src.models.fix.generated.components.trdgsesgrp import TrdgSesGrp

class MarketDataRequest(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    mdreqid: str = Field(..., description='', alias='262')
    subscriptionrequesttype: str = Field(..., description='', alias='263')
    marketdepth: int = Field(..., description='', alias='264')
    mdupdatetype: Optional[int] = Field(None, description='', alias='265')
    aggregatedbook: Optional[bool] = Field(None, description='', alias='266')
    openclosesettlflag: Optional[List[str]] = Field(None, description='', alias='286')
    scope: Optional[List[str]] = Field(None, description='', alias='546')
    mdimplicitdelete: Optional[bool] = Field(None, description='', alias='547')
    applqueueaction: Optional[int] = Field(None, description='', alias='815')
    applqueuemax: Optional[int] = Field(None, description='', alias='812')
    mdreqgrp: MDReqGrp = Field(..., description='MDReqGrp component')
    instrmtmdreqgrp: InstrmtMDReqGrp = Field(..., description='InstrmtMDReqGrp component')
    trdgsesgrp: Optional[TrdgSesGrp] = Field(None, description='TrdgSesGrp component')

