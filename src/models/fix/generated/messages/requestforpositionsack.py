from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.parties import Parties
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp

class RequestForPositionsAck(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    posmaintrptid: str = Field(..., description='', alias='721')
    posreqid: Optional[str] = Field(None, description='', alias='710')
    totalnumposreports: Optional[int] = Field(None, description='', alias='727')
    unsolicitedindicator: Optional[bool] = Field(None, description='', alias='325')
    posreqresult: int = Field(..., description='', alias='728')
    posreqstatus: int = Field(..., description='', alias='729')
    account: str = Field(..., description='', alias='1')
    acctidsource: Optional[int] = Field(None, description='', alias='660')
    accounttype: int = Field(..., description='', alias='581')
    currency: Optional[str] = Field(None, description='', alias='15')
    responsetransporttype: Optional[int] = Field(None, description='', alias='725')
    responsedestination: Optional[str] = Field(None, description='', alias='726')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedtextlen: Optional[int] = Field(None, description='', alias='354')
    encodedtext: Optional[str] = Field(None, description='', alias='355')
    parties: Parties = Field(..., description='Parties component')
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    instrmtleggrp: Optional[InstrmtLegGrp] = Field(None, description='InstrmtLegGrp component')
    undinstrmtgrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')

