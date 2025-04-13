from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.compidreqgrp import CompIDReqGrp

class NetworkCounterpartySystemStatusRequest(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    networkrequesttype: int = Field(..., description='', alias='935')
    networkrequestid: str = Field(..., description='', alias='933')
    compidreqgrp: Optional[CompIDReqGrp] = Field(None, description='CompIDReqGrp component')

