from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.instrmtstrkpxgrp import InstrmtStrkPxGrp
from src.models.fix.generated.components.undinstrmtstrkpxgrp import UndInstrmtStrkPxGrp

class ListStrikePrice(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    listid: str = Field(..., description='', alias='66')
    totnostrikes: int = Field(..., description='', alias='422')
    lastfragment: Optional[bool] = Field(None, description='', alias='893')
    instrmtstrkpxgrp: InstrmtStrkPxGrp = Field(..., description='InstrmtStrkPxGrp component')
    undinstrmtstrkpxgrp: Optional[UndInstrmtStrkPxGrp] = Field(None, description='UndInstrmtStrkPxGrp component')

