from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.instrumentextension import InstrumentExtension
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp

class SecurityStatus(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    securitystatusreqid: Optional[str] = Field(None, description='', alias='324')
    currency: Optional[str] = Field(None, description='', alias='15')
    tradingsessionid: Optional[str] = Field(None, description='', alias='336')
    tradingsessionsubid: Optional[str] = Field(None, description='', alias='625')
    unsolicitedindicator: Optional[bool] = Field(None, description='', alias='325')
    securitytradingstatus: Optional[int] = Field(None, description='', alias='326')
    financialstatus: Optional[List[str]] = Field(None, description='', alias='291')
    corporateaction: Optional[List[str]] = Field(None, description='', alias='292')
    haltreasonchar: Optional[str] = Field(None, description='', alias='327')
    inviewofcommon: Optional[bool] = Field(None, description='', alias='328')
    duetorelated: Optional[bool] = Field(None, description='', alias='329')
    buyvolume: Optional[float] = Field(None, description='', alias='330')
    sellvolume: Optional[float] = Field(None, description='', alias='331')
    highpx: Optional[float] = Field(None, description='', alias='332')
    lowpx: Optional[float] = Field(None, description='', alias='333')
    lastpx: Optional[float] = Field(None, description='', alias='31')
    transacttime: Optional[datetime] = Field(None, description='', alias='60')
    adjustment: Optional[int] = Field(None, description='', alias='334')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedtextlen: Optional[int] = Field(None, description='', alias='354')
    encodedtext: Optional[str] = Field(None, description='', alias='355')
    instrument: Instrument = Field(..., description='Instrument component')
    instrumentextension: Optional[InstrumentExtension] = Field(None, description='InstrumentExtension component')
    undinstrmtgrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    instrmtleggrp: Optional[InstrmtLegGrp] = Field(None, description='InstrmtLegGrp component')

