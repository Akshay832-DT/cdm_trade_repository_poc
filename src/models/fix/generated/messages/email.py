"""FIX message model for Email (C).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.instrmtgrp import InstrmtGrpComponent
from ..components.instrmtleggrp import InstrmtLegGrpComponent
from ..components.linesoftextgrp import LinesOfTextGrpComponent
from ..components.routinggrp import RoutingGrpComponent
from ..components.undinstrmtgrp import UndInstrmtGrpComponent

class EmailMessage(FIXMessageBase):
    """FIX message model for Email."""

    MsgType: str = Field("C", alias="35")

    EmailThreadID: str = Field(..., alias='164', description='')
    EmailType: str = Field(..., alias='94', description='')
    OrigTime: Optional[datetime] = Field(None, alias='42', description='')
    Subject: str = Field(..., alias='147', description='')
    EncodedSubjectLen: Optional[int] = Field(None, alias='356', description='')
    EncodedSubject: Optional[str] = Field(None, alias='357', description='')
    OrderID: Optional[str] = Field(None, alias='37', description='')
    ClOrdID: Optional[str] = Field(None, alias='11', description='')
    RawDataLength: Optional[int] = Field(None, alias='95', description='')
    RawData: Optional[str] = Field(None, alias='96', description='')
    RoutingGrp: Optional[RoutingGrpComponent] = Field(None, description='')
    InstrmtGrp: Optional[InstrmtGrpComponent] = Field(None, description='')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='')
    LinesOfTextGrp: LinesOfTextGrpComponent = Field(..., description='')

