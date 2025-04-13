from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp
from src.models.fix.generated.components.orderqtydata import OrderQtyData

class DontKnowTrade(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    orderid: str = Field(..., description='', alias='37')
    secondaryorderid: Optional[str] = Field(None, description='', alias='198')
    execid: str = Field(..., description='', alias='17')
    dkreason: str = Field(..., description='', alias='127')
    side: str = Field(..., description='', alias='54')
    lastqty: Optional[float] = Field(None, description='', alias='32')
    lastpx: Optional[float] = Field(None, description='', alias='31')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedtextlen: Optional[int] = Field(None, description='', alias='354')
    encodedtext: Optional[str] = Field(None, description='', alias='355')
    instrument: Instrument = Field(..., description='Instrument component')
    undinstrmtgrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    instrmtleggrp: Optional[InstrmtLegGrp] = Field(None, description='InstrmtLegGrp component')
    orderqtydata: OrderQtyData = Field(..., description='OrderQtyData component')

