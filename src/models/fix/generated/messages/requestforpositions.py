"""FIX message model for RequestForPositions (AN).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.instrmtleggrp import InstrmtLegGrpComponent
from ..components.instrument import InstrumentComponent
from ..components.parties import PartiesComponent
from ..components.trdgsesgrp import TrdgSesGrpComponent
from ..components.undinstrmtgrp import UndInstrmtGrpComponent

class RequestForPositionsMessage(FIXMessageBase):
    """FIX message model for RequestForPositions."""

    MsgType: str = Field("AN", alias="35")

    PosReqID: str = Field(..., alias='710', description='')
    PosReqType: int = Field(..., alias='724', description='')
    MatchStatus: Optional[str] = Field(None, alias='573', description='')
    SubscriptionRequestType: Optional[str] = Field(None, alias='263', description='')
    Account: str = Field(..., alias='1', description='')
    AcctIDSource: Optional[int] = Field(None, alias='660', description='')
    AccountType: int = Field(..., alias='581', description='')
    Currency: Optional[str] = Field(None, alias='15', description='')
    ClearingBusinessDate: date = Field(..., alias='715', description='')
    SettlSessID: Optional[str] = Field(None, alias='716', description='')
    SettlSessSubID: Optional[str] = Field(None, alias='717', description='')
    TransactTime: datetime = Field(..., alias='60', description='')
    ResponseTransportType: Optional[int] = Field(None, alias='725', description='')
    ResponseDestination: Optional[str] = Field(None, alias='726', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    Parties: PartiesComponent = Field(..., description='')
    Instrument: Optional[InstrumentComponent] = Field(None, description='')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')
    TrdgSesGrp: Optional[TrdgSesGrpComponent] = Field(None, description='')

