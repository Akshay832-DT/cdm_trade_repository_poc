from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.routinggrp import RoutingGrpComponent
from src.models.fix.generated.components.instrmtgrp import InstrmtGrpComponent
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrpComponent
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrpComponent
from src.models.fix.generated.components.linesoftextgrp import LinesOfTextGrpComponent

class Email(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    EmailThreadID: str = Field(..., description='', alias='164')
    EmailType: str = Field(..., description='', alias='94')
    OrigTime: Optional[datetime] = Field(None, description='', alias='42')
    Subject: str = Field(..., description='', alias='147')
    EncodedSubjectLen: Optional[int] = Field(None, description='', alias='356')
    EncodedSubject: Optional[str] = Field(None, description='', alias='357')
    OrderID: Optional[str] = Field(None, description='', alias='37')
    ClOrdID: Optional[str] = Field(None, description='', alias='11')
    RawDataLength: Optional[int] = Field(None, description='', alias='95')
    RawData: Optional[str] = Field(None, description='', alias='96')
    RoutingGrp: Optional[RoutingGrpComponent] = Field(None, description='RoutingGrp component')
    InstrmtGrp: Optional[InstrmtGrpComponent] = Field(None, description='InstrmtGrp component')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='UndInstrmtGrp component')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='InstrmtLegGrp component')
    LinesOfTextGrp: LinesOfTextGrpComponent = Field(..., description='LinesOfTextGrp component')

