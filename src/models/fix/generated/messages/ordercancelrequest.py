from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.parties import Parties
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.financingdetails import FinancingDetails
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp
from src.models.fix.generated.components.orderqtydata import OrderQtyData

class OrderCancelRequest(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    origclordid: str = Field(..., description='', alias='41')
    orderid: Optional[str] = Field(None, description='', alias='37')
    clordid: str = Field(..., description='', alias='11')
    secondaryclordid: Optional[str] = Field(None, description='', alias='526')
    clordlinkid: Optional[str] = Field(None, description='', alias='583')
    listid: Optional[str] = Field(None, description='', alias='66')
    origordmodtime: Optional[datetime] = Field(None, description='', alias='586')
    account: Optional[str] = Field(None, description='', alias='1')
    acctidsource: Optional[int] = Field(None, description='', alias='660')
    accounttype: Optional[int] = Field(None, description='', alias='581')
    side: str = Field(..., description='', alias='54')
    transacttime: datetime = Field(..., description='', alias='60')
    complianceid: Optional[str] = Field(None, description='', alias='376')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedtextlen: Optional[int] = Field(None, description='', alias='354')
    encodedtext: Optional[str] = Field(None, description='', alias='355')
    parties: Optional[Parties] = Field(None, description='Parties component')
    instrument: Instrument = Field(..., description='Instrument component')
    financingdetails: Optional[FinancingDetails] = Field(None, description='FinancingDetails component')
    undinstrmtgrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    orderqtydata: OrderQtyData = Field(..., description='OrderQtyData component')

