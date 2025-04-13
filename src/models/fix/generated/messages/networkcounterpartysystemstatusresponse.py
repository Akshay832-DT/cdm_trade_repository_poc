from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.compidstatgrp import CompIDStatGrpComponent

class NetworkCounterpartySystemStatusResponse(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    NetworkStatusResponseType: int = Field(..., description='', alias='937')
    NetworkRequestID: Optional[str] = Field(None, description='', alias='933')
    NetworkResponseID: str = Field(..., description='', alias='932')
    LastNetworkResponseID: Optional[str] = Field(None, description='', alias='934')
    CompIDStatGrp: CompIDStatGrpComponent = Field(..., description='CompIDStatGrp component')

