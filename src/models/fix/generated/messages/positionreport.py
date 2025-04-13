from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.parties import Parties
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp
from src.models.fix.generated.components.posundinstrmtgrp import PosUndInstrmtGrp
from src.models.fix.generated.components.positionqty import PositionQty
from src.models.fix.generated.components.positionamountdata import PositionAmountData

class PositionReport(FIXMessageBase):
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
    posreqtype: Optional[int] = Field(None, description='', alias='724')
    subscriptionrequesttype: Optional[str] = Field(None, description='', alias='263')
    totalnumposreports: Optional[int] = Field(None, description='', alias='727')
    unsolicitedindicator: Optional[bool] = Field(None, description='', alias='325')
    posreqresult: int = Field(..., description='', alias='728')
    clearingbusinessdate: date = Field(..., description='', alias='715')
    settlsessid: Optional[str] = Field(None, description='', alias='716')
    settlsesssubid: Optional[str] = Field(None, description='', alias='717')
    account: str = Field(..., description='', alias='1')
    acctidsource: Optional[int] = Field(None, description='', alias='660')
    accounttype: int = Field(..., description='', alias='581')
    currency: Optional[str] = Field(None, description='', alias='15')
    settlprice: float = Field(..., description='', alias='730')
    settlpricetype: int = Field(..., description='', alias='731')
    priorsettlprice: float = Field(..., description='', alias='734')
    registstatus: Optional[str] = Field(None, description='', alias='506')
    deliverydate: Optional[date] = Field(None, description='', alias='743')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedtextlen: Optional[int] = Field(None, description='', alias='354')
    encodedtext: Optional[str] = Field(None, description='', alias='355')
    parties: Parties = Field(..., description='Parties component')
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    instrmtleggrp: Optional[InstrmtLegGrp] = Field(None, description='InstrmtLegGrp component')
    posundinstrmtgrp: Optional[PosUndInstrmtGrp] = Field(None, description='PosUndInstrmtGrp component')
    positionqty: PositionQty = Field(..., description='PositionQty component')
    positionamountdata: PositionAmountData = Field(..., description='PositionAmountData component')

