from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.parties import Parties
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp
from src.models.fix.generated.components.positionqty import PositionQty
from src.models.fix.generated.components.positionamountdata import PositionAmountData

class AssignmentReport(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    asgnrptid: str = Field(..., description='', alias='833')
    totnumassignmentreports: Optional[int] = Field(None, description='', alias='832')
    lastrptrequested: Optional[bool] = Field(None, description='', alias='912')
    account: Optional[str] = Field(None, description='', alias='1')
    accounttype: int = Field(..., description='', alias='581')
    currency: Optional[str] = Field(None, description='', alias='15')
    thresholdamount: Optional[float] = Field(None, description='', alias='834')
    settlprice: float = Field(..., description='', alias='730')
    settlpricetype: int = Field(..., description='', alias='731')
    underlyingsettlprice: float = Field(..., description='', alias='732')
    expiredate: Optional[date] = Field(None, description='', alias='432')
    assignmentmethod: str = Field(..., description='', alias='744')
    assignmentunit: Optional[float] = Field(None, description='', alias='745')
    openinterest: float = Field(..., description='', alias='746')
    exercisemethod: str = Field(..., description='', alias='747')
    settlsessid: str = Field(..., description='', alias='716')
    settlsesssubid: str = Field(..., description='', alias='717')
    clearingbusinessdate: date = Field(..., description='', alias='715')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedtextlen: Optional[int] = Field(None, description='', alias='354')
    encodedtext: Optional[str] = Field(None, description='', alias='355')
    parties: Parties = Field(..., description='Parties component')
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    instrmtleggrp: Optional[InstrmtLegGrp] = Field(None, description='InstrmtLegGrp component')
    undinstrmtgrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    positionqty: PositionQty = Field(..., description='PositionQty component')
    positionamountdata: PositionAmountData = Field(..., description='PositionAmountData component')

