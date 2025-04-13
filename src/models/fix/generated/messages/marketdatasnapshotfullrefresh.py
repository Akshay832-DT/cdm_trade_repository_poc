from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp
from src.models.fix.generated.components.mdfullgrp import MDFullGrp

class MarketDataSnapshotFullRefresh(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    mdreqid: Optional[str] = Field(None, description='', alias='262')
    financialstatus: Optional[List[str]] = Field(None, description='', alias='291')
    corporateaction: Optional[List[str]] = Field(None, description='', alias='292')
    netchgprevday: Optional[float] = Field(None, description='', alias='451')
    applqueuedepth: Optional[int] = Field(None, description='', alias='813')
    applqueueresolution: Optional[int] = Field(None, description='', alias='814')
    instrument: Instrument = Field(..., description='Instrument component')
    undinstrmtgrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    instrmtleggrp: Optional[InstrmtLegGrp] = Field(None, description='InstrmtLegGrp component')
    mdfullgrp: MDFullGrp = Field(..., description='MDFullGrp component')

