from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp

class Advertisement(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    advid: str = Field(..., description='', alias='2')
    advtranstype: str = Field(..., description='', alias='5')
    advrefid: Optional[str] = Field(None, description='', alias='3')
    advside: str = Field(..., description='', alias='4')
    quantity: float = Field(..., description='', alias='53')
    qtytype: Optional[int] = Field(None, description='', alias='854')
    price: Optional[float] = Field(None, description='', alias='44')
    currency: Optional[str] = Field(None, description='', alias='15')
    tradedate: Optional[date] = Field(None, description='', alias='75')
    transacttime: Optional[datetime] = Field(None, description='', alias='60')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedtextlen: Optional[int] = Field(None, description='', alias='354')
    encodedtext: Optional[str] = Field(None, description='', alias='355')
    urllink: Optional[str] = Field(None, description='', alias='149')
    lastmkt: Optional[str] = Field(None, description='', alias='30')
    tradingsessionid: Optional[str] = Field(None, description='', alias='336')
    tradingsessionsubid: Optional[str] = Field(None, description='', alias='625')
    instrument: Instrument = Field(..., description='Instrument component')
    instrmtleggrp: Optional[InstrmtLegGrp] = Field(None, description='InstrmtLegGrp component')
    undinstrmtgrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')

