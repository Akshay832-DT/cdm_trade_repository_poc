from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.seclistgrp import SecListGrp

class SecurityList(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    securityreqid: str = Field(..., description='', alias='320')
    securityresponseid: str = Field(..., description='', alias='322')
    securityrequestresult: int = Field(..., description='', alias='560')
    totnorelatedsym: Optional[int] = Field(None, description='', alias='393')
    lastfragment: Optional[bool] = Field(None, description='', alias='893')
    seclistgrp: Optional[SecListGrp] = Field(None, description='SecListGrp component')

