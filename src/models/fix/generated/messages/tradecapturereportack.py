from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.trdregtimestamps import TrdRegTimestamps
from src.models.fix.generated.components.trdinstrmtleggrp import TrdInstrmtLegGrp
from src.models.fix.generated.components.trdallocgrp import TrdAllocGrp

class TradeCaptureReportAck(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    tradereportid: str = Field(..., description='', alias='571')
    tradereporttranstype: Optional[int] = Field(None, description='', alias='487')
    tradereporttype: Optional[int] = Field(None, description='', alias='856')
    trdtype: Optional[int] = Field(None, description='', alias='828')
    trdsubtype: Optional[int] = Field(None, description='', alias='829')
    secondarytrdtype: Optional[int] = Field(None, description='', alias='855')
    transferreason: Optional[str] = Field(None, description='', alias='830')
    exectype: str = Field(..., description='', alias='150')
    tradereportrefid: Optional[str] = Field(None, description='', alias='572')
    secondarytradereportrefid: Optional[str] = Field(None, description='', alias='881')
    trdrptstatus: Optional[int] = Field(None, description='', alias='939')
    tradereportrejectreason: Optional[int] = Field(None, description='', alias='751')
    secondarytradereportid: Optional[str] = Field(None, description='', alias='818')
    subscriptionrequesttype: Optional[str] = Field(None, description='', alias='263')
    tradelinkid: Optional[str] = Field(None, description='', alias='820')
    trdmatchid: Optional[str] = Field(None, description='', alias='880')
    execid: Optional[str] = Field(None, description='', alias='17')
    secondaryexecid: Optional[str] = Field(None, description='', alias='527')
    transacttime: Optional[datetime] = Field(None, description='', alias='60')
    responsetransporttype: Optional[int] = Field(None, description='', alias='725')
    responsedestination: Optional[str] = Field(None, description='', alias='726')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedtextlen: Optional[int] = Field(None, description='', alias='354')
    encodedtext: Optional[str] = Field(None, description='', alias='355')
    clearingfeeindicator: Optional[str] = Field(None, description='', alias='635')
    ordercapacity: Optional[str] = Field(None, description='', alias='528')
    orderrestrictions: Optional[List[str]] = Field(None, description='', alias='529')
    custordercapacity: Optional[int] = Field(None, description='', alias='582')
    account: Optional[str] = Field(None, description='', alias='1')
    acctidsource: Optional[int] = Field(None, description='', alias='660')
    accounttype: Optional[int] = Field(None, description='', alias='581')
    positioneffect: Optional[str] = Field(None, description='', alias='77')
    preallocmethod: Optional[str] = Field(None, description='', alias='591')
    instrument: Instrument = Field(..., description='Instrument component')
    trdregtimestamps: Optional[TrdRegTimestamps] = Field(None, description='TrdRegTimestamps component')
    trdinstrmtleggrp: Optional[TrdInstrmtLegGrp] = Field(None, description='TrdInstrmtLegGrp component')
    trdallocgrp: Optional[TrdAllocGrp] = Field(None, description='TrdAllocGrp component')

