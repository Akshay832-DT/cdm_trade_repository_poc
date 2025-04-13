from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.affectedordgrp import AffectedOrdGrp
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.underlyinginstrument import UnderlyingInstrument

class OrderMassCancelReport(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    clordid: Optional[str] = Field(None, description='', alias='11')
    secondaryclordid: Optional[str] = Field(None, description='', alias='526')
    orderid: str = Field(..., description='', alias='37')
    secondaryorderid: Optional[str] = Field(None, description='', alias='198')
    masscancelrequesttype: str = Field(..., description='', alias='530')
    masscancelresponse: str = Field(..., description='', alias='531')
    masscancelrejectreason: Optional[str] = Field(None, description='', alias='532')
    totalaffectedorders: Optional[int] = Field(None, description='', alias='533')
    tradingsessionid: Optional[str] = Field(None, description='', alias='336')
    tradingsessionsubid: Optional[str] = Field(None, description='', alias='625')
    side: Optional[str] = Field(None, description='', alias='54')
    transacttime: Optional[datetime] = Field(None, description='', alias='60')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedtextlen: Optional[int] = Field(None, description='', alias='354')
    encodedtext: Optional[str] = Field(None, description='', alias='355')
    affectedordgrp: Optional[AffectedOrdGrp] = Field(None, description='AffectedOrdGrp component')
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    underlyinginstrument: Optional[UnderlyingInstrument] = Field(None, description='UnderlyingInstrument component')

