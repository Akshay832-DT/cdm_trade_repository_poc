from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.sidecrossordcxlgrp import SideCrossOrdCxlGrp
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp

class CrossOrderCancelRequest(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    orderid: Optional[str] = Field(None, description='', alias='37')
    crossid: str = Field(..., description='', alias='548')
    origcrossid: str = Field(..., description='', alias='551')
    crosstype: int = Field(..., description='', alias='549')
    crossprioritization: int = Field(..., description='', alias='550')
    transacttime: datetime = Field(..., description='', alias='60')
    sidecrossordcxlgrp: SideCrossOrdCxlGrp = Field(..., description='SideCrossOrdCxlGrp component')
    instrument: Instrument = Field(..., description='Instrument component')
    undinstrmtgrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    instrmtleggrp: Optional[InstrmtLegGrp] = Field(None, description='InstrmtLegGrp component')

