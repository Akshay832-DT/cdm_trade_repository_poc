from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.rfqreqgrp import RFQReqGrp

class RFQRequest(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    rfqreqid: str = Field(..., description='', alias='644')
    subscriptionrequesttype: Optional[str] = Field(None, description='', alias='263')
    rfqreqgrp: RFQReqGrp = Field(..., description='RFQReqGrp component')

