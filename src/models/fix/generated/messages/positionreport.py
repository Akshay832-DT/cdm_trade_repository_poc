from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.parties import PartiesComponent
from src.models.fix.generated.components.instrument import InstrumentComponent
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrpComponent
from src.models.fix.generated.components.posundinstrmtgrp import PosUndInstrmtGrpComponent
from src.models.fix.generated.components.positionqty import PositionQtyComponent
from src.models.fix.generated.components.positionamountdata import PositionAmountDataComponent

class PositionReport(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    PosMaintRptID: str = Field(..., description='', alias='721')
    PosReqID: Optional[str] = Field(None, description='', alias='710')
    PosReqType: Optional[int] = Field(None, description='', alias='724')
    SubscriptionRequestType: Optional[str] = Field(None, description='', alias='263')
    TotalNumPosReports: Optional[int] = Field(None, description='', alias='727')
    UnsolicitedIndicator: Optional[bool] = Field(None, description='', alias='325')
    PosReqResult: int = Field(..., description='', alias='728')
    ClearingBusinessDate: date = Field(..., description='', alias='715')
    SettlSessID: Optional[str] = Field(None, description='', alias='716')
    SettlSessSubID: Optional[str] = Field(None, description='', alias='717')
    Account: str = Field(..., description='', alias='1')
    AcctIDSource: Optional[int] = Field(None, description='', alias='660')
    AccountType: int = Field(..., description='', alias='581')
    Currency: Optional[str] = Field(None, description='', alias='15')
    SettlPrice: float = Field(..., description='', alias='730')
    SettlPriceType: int = Field(..., description='', alias='731')
    PriorSettlPrice: float = Field(..., description='', alias='734')
    RegistStatus: Optional[str] = Field(None, description='', alias='506')
    DeliveryDate: Optional[date] = Field(None, description='', alias='743')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    Parties: PartiesComponent = Field(..., description='Parties component')
    Instrument: Optional[InstrumentComponent] = Field(None, description='Instrument component')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='InstrmtLegGrp component')
    PosUndInstrmtGrp: Optional[PosUndInstrmtGrpComponent] = Field(None, description='PosUndInstrmtGrp component')
    PositionQty: PositionQtyComponent = Field(..., description='PositionQty component')
    PositionAmountData: PositionAmountDataComponent = Field(..., description='PositionAmountData component')

