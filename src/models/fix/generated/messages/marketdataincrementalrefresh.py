from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.mdincgrp import MDIncGrp

class MarketDataIncrementalRefresh(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    mdreqid: Optional[str] = Field(None, description='', alias='262')
    applqueuedepth: Optional[int] = Field(None, description='', alias='813')
    applqueueresolution: Optional[int] = Field(None, description='', alias='814')
    mdincgrp: MDIncGrp = Field(..., description='MDIncGrp component')

