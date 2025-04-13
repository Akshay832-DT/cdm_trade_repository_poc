from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.instrmtstrkpxgrp import InstrmtStrkPxGrpComponent
from src.models.fix.generated.components.undinstrmtstrkpxgrp import UndInstrmtStrkPxGrpComponent

class ListStrikePrice(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    ListID: str = Field(..., description='', alias='66')
    TotNoStrikes: int = Field(..., description='', alias='422')
    LastFragment: Optional[bool] = Field(None, description='', alias='893')
    InstrmtStrkPxGrp: InstrmtStrkPxGrpComponent = Field(..., description='InstrmtStrkPxGrp component')
    UndInstrmtStrkPxGrp: Optional[UndInstrmtStrkPxGrpComponent] = Field(None, description='UndInstrmtStrkPxGrp component')

