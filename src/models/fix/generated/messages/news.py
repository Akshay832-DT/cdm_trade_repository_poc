"""FIX message model for News (B).

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

class NewsMessage(FIXMessageBase):
    """FIX message model for News."""

    MsgType: str = Field("B", alias="35")

    OrigTime: Optional[datetime] = Field(None, alias='42', description='')
    Urgency: Optional[str] = Field(None, alias='61', description='')
    Headline: str = Field(..., alias='148', description='')
    EncodedHeadlineLen: Optional[int] = Field(None, alias='358', description='')
    EncodedHeadline: Optional[str] = Field(None, alias='359', description='')
    URLLink: Optional[str] = Field(None, alias='149', description='')
    RawDataLength: Optional[int] = Field(None, alias='95', description='')
    RawData: Optional[str] = Field(None, alias='96', description='')
    RoutingGrp: Optional[RoutingGrpComponent] = Field(None, description='')
    InstrmtGrp: Optional[InstrmtGrpComponent] = Field(None, description='')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')
    LinesOfTextGrp: LinesOfTextGrpComponent = Field(..., description='')

