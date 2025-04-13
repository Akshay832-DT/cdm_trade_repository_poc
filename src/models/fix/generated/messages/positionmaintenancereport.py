from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.parties import Parties
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp
from src.models.fix.generated.components.trdgsesgrp import TrdgSesGrp
from src.models.fix.generated.components.positionqty import PositionQty
from src.models.fix.generated.components.positionamountdata import PositionAmountData

class PositionMaintenanceReport(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    posmaintrptid: str = Field(..., description='', alias='721')
    postranstype: int = Field(..., description='', alias='709')
    posreqid: Optional[str] = Field(None, description='', alias='710')
    posmaintaction: int = Field(..., description='', alias='712')
    origposreqrefid: str = Field(..., description='', alias='713')
    posmaintstatus: int = Field(..., description='', alias='722')
    posmaintresult: Optional[int] = Field(None, description='', alias='723')
    clearingbusinessdate: date = Field(..., description='', alias='715')
    settlsessid: Optional[str] = Field(None, description='', alias='716')
    settlsesssubid: Optional[str] = Field(None, description='', alias='717')
    account: str = Field(..., description='', alias='1')
    acctidsource: Optional[int] = Field(None, description='', alias='660')
    accounttype: int = Field(..., description='', alias='581')
    currency: Optional[str] = Field(None, description='', alias='15')
    transacttime: datetime = Field(..., description='', alias='60')
    adjustmenttype: Optional[int] = Field(None, description='', alias='718')
    thresholdamount: Optional[float] = Field(None, description='', alias='834')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedtextlen: Optional[int] = Field(None, description='', alias='354')
    encodedtext: Optional[str] = Field(None, description='', alias='355')
    parties: Optional[Parties] = Field(None, description='Parties component')
    instrument: Instrument = Field(..., description='Instrument component')
    instrmtleggrp: Optional[InstrmtLegGrp] = Field(None, description='InstrmtLegGrp component')
    undinstrmtgrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    trdgsesgrp: Optional[TrdgSesGrp] = Field(None, description='TrdgSesGrp component')
    positionqty: PositionQty = Field(..., description='PositionQty component')
    positionamountdata: PositionAmountData = Field(..., description='PositionAmountData component')

