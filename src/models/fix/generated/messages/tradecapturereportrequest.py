from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.parties import Parties
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.instrumentextension import InstrumentExtension
from src.models.fix.generated.components.financingdetails import FinancingDetails
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp
from src.models.fix.generated.components.trdcapdtgrp import TrdCapDtGrp

class TradeCaptureReportRequest(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    traderequestid: str = Field(..., description='', alias='568')
    traderequesttype: int = Field(..., description='', alias='569')
    subscriptionrequesttype: Optional[str] = Field(None, description='', alias='263')
    tradereportid: Optional[str] = Field(None, description='', alias='571')
    secondarytradereportid: Optional[str] = Field(None, description='', alias='818')
    execid: Optional[str] = Field(None, description='', alias='17')
    exectype: Optional[str] = Field(None, description='', alias='150')
    orderid: Optional[str] = Field(None, description='', alias='37')
    clordid: Optional[str] = Field(None, description='', alias='11')
    matchstatus: Optional[str] = Field(None, description='', alias='573')
    trdtype: Optional[int] = Field(None, description='', alias='828')
    trdsubtype: Optional[int] = Field(None, description='', alias='829')
    transferreason: Optional[str] = Field(None, description='', alias='830')
    secondarytrdtype: Optional[int] = Field(None, description='', alias='855')
    tradelinkid: Optional[str] = Field(None, description='', alias='820')
    trdmatchid: Optional[str] = Field(None, description='', alias='880')
    clearingbusinessdate: Optional[date] = Field(None, description='', alias='715')
    tradingsessionid: Optional[str] = Field(None, description='', alias='336')
    tradingsessionsubid: Optional[str] = Field(None, description='', alias='625')
    timebracket: Optional[str] = Field(None, description='', alias='943')
    side: Optional[str] = Field(None, description='', alias='54')
    multilegreportingtype: Optional[str] = Field(None, description='', alias='442')
    tradeinputsource: Optional[str] = Field(None, description='', alias='578')
    tradeinputdevice: Optional[str] = Field(None, description='', alias='579')
    responsetransporttype: Optional[int] = Field(None, description='', alias='725')
    responsedestination: Optional[str] = Field(None, description='', alias='726')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedtextlen: Optional[int] = Field(None, description='', alias='354')
    encodedtext: Optional[str] = Field(None, description='', alias='355')
    parties: Optional[Parties] = Field(None, description='Parties component')
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    instrumentextension: Optional[InstrumentExtension] = Field(None, description='InstrumentExtension component')
    financingdetails: Optional[FinancingDetails] = Field(None, description='FinancingDetails component')
    undinstrmtgrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    instrmtleggrp: Optional[InstrmtLegGrp] = Field(None, description='InstrmtLegGrp component')
    trdcapdtgrp: Optional[TrdCapDtGrp] = Field(None, description='TrdCapDtGrp component')

