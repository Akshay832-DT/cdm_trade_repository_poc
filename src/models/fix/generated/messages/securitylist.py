from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.seclistgrp import SecListGrpComponent

class SecurityList(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    SecurityReqID: str = Field(..., description='', alias='320')
    SecurityResponseID: str = Field(..., description='', alias='322')
    SecurityRequestResult: int = Field(..., description='', alias='560')
    TotNoRelatedSym: Optional[int] = Field(None, description='', alias='393')
    LastFragment: Optional[bool] = Field(None, description='', alias='893')
    SecListGrp: Optional[SecListGrpComponent] = Field(None, description='SecListGrp component')

