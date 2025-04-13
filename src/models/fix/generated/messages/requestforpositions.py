from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.parties import PartiesComponent
from src.models.fix.generated.components.instrument import InstrumentComponent
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrpComponent
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrpComponent
from src.models.fix.generated.components.trdgsesgrp import TrdgSesGrpComponent

class RequestForPositions(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    PosReqID: str = Field(..., description='', alias='710')
    PosReqType: int = Field(..., description='', alias='724')
    MatchStatus: Optional[str] = Field(None, description='', alias='573')
    SubscriptionRequestType: Optional[str] = Field(None, description='', alias='263')
    Account: str = Field(..., description='', alias='1')
    AcctIDSource: Optional[int] = Field(None, description='', alias='660')
    AccountType: int = Field(..., description='', alias='581')
    Currency: Optional[str] = Field(None, description='', alias='15')
    ClearingBusinessDate: date = Field(..., description='', alias='715')
    SettlSessID: Optional[str] = Field(None, description='', alias='716')
    SettlSessSubID: Optional[str] = Field(None, description='', alias='717')
    TransactTime: datetime = Field(..., description='', alias='60')
    ResponseTransportType: Optional[int] = Field(None, description='', alias='725')
    ResponseDestination: Optional[str] = Field(None, description='', alias='726')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    Parties: PartiesComponent = Field(..., description='Parties component')
    Instrument: Optional[InstrumentComponent] = Field(None, description='Instrument component')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='InstrmtLegGrp component')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='UndInstrmtGrp component')
    TrdgSesGrp: Optional[TrdgSesGrpComponent] = Field(None, description='TrdgSesGrp component')

