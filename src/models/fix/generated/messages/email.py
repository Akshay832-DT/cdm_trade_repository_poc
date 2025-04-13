from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.routinggrp import RoutingGrp
from src.models.fix.generated.components.instrmtgrp import InstrmtGrp
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp
from src.models.fix.generated.components.linesoftextgrp import LinesOfTextGrp

class Email(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    emailthreadid: str = Field(..., description='', alias='164')
    emailtype: str = Field(..., description='', alias='94')
    origtime: Optional[datetime] = Field(None, description='', alias='42')
    subject: str = Field(..., description='', alias='147')
    encodedsubjectlen: Optional[int] = Field(None, description='', alias='356')
    encodedsubject: Optional[str] = Field(None, description='', alias='357')
    orderid: Optional[str] = Field(None, description='', alias='37')
    clordid: Optional[str] = Field(None, description='', alias='11')
    rawdatalength: Optional[int] = Field(None, description='', alias='95')
    rawdata: Optional[str] = Field(None, description='', alias='96')
    routinggrp: Optional[RoutingGrp] = Field(None, description='RoutingGrp component')
    instrmtgrp: Optional[InstrmtGrp] = Field(None, description='InstrmtGrp component')
    undinstrmtgrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    instrmtleggrp: Optional[InstrmtLegGrp] = Field(None, description='InstrmtLegGrp component')
    linesoftextgrp: LinesOfTextGrp = Field(..., description='LinesOfTextGrp component')

