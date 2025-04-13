from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.instrumentextension import InstrumentExtension
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp

class SecurityDefinition(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    securityreqid: str = Field(..., description='', alias='320')
    securityresponseid: str = Field(..., description='', alias='322')
    securityresponsetype: int = Field(..., description='', alias='323')
    currency: Optional[str] = Field(None, description='', alias='15')
    tradingsessionid: Optional[str] = Field(None, description='', alias='336')
    tradingsessionsubid: Optional[str] = Field(None, description='', alias='625')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedtextlen: Optional[int] = Field(None, description='', alias='354')
    encodedtext: Optional[str] = Field(None, description='', alias='355')
    expirationcycle: Optional[int] = Field(None, description='', alias='827')
    roundlot: Optional[float] = Field(None, description='', alias='561')
    mintradevol: Optional[float] = Field(None, description='', alias='562')
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    instrumentextension: Optional[InstrumentExtension] = Field(None, description='InstrumentExtension component')
    undinstrmtgrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    instrmtleggrp: Optional[InstrmtLegGrp] = Field(None, description='InstrmtLegGrp component')

