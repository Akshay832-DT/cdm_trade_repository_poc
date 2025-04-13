from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.routinggrp import RoutingGrpComponent
from src.models.fix.generated.components.instrmtgrp import InstrmtGrpComponent
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrpComponent
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrpComponent
from src.models.fix.generated.components.linesoftextgrp import LinesOfTextGrpComponent

class News(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    OrigTime: Optional[datetime] = Field(None, description='', alias='42')
    Urgency: Optional[str] = Field(None, description='', alias='61')
    Headline: str = Field(..., description='', alias='148')
    EncodedHeadlineLen: Optional[int] = Field(None, description='', alias='358')
    EncodedHeadline: Optional[str] = Field(None, description='', alias='359')
    URLLink: Optional[str] = Field(None, description='', alias='149')
    RawDataLength: Optional[int] = Field(None, description='', alias='95')
    RawData: Optional[str] = Field(None, description='', alias='96')
    RoutingGrp: Optional[RoutingGrpComponent] = Field(None, description='RoutingGrp component')
    InstrmtGrp: Optional[InstrmtGrpComponent] = Field(None, description='InstrmtGrp component')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='InstrmtLegGrp component')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='UndInstrmtGrp component')
    LinesOfTextGrp: LinesOfTextGrpComponent = Field(..., description='LinesOfTextGrp component')

