"""FIX message model for PositionReport (AP).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.instrmtleggrp import InstrmtLegGrpComponent
from ..components.instrument import InstrumentComponent
from ..components.parties import PartiesComponent
from ..components.posundinstrmtgrp import PosUndInstrmtGrpComponent
from ..components.positionamountdata import PositionAmountDataComponent
from ..components.positionqty import PositionQtyComponent

class PositionReportMessage(FIXMessageBase):
    """FIX message model for PositionReport."""

    MsgType: str = Field("AP", alias="35")

    PosMaintRptID: str = Field(..., alias='721', description='')
    PosReqID: Optional[str] = Field(None, alias='710', description='')
    PosReqType: Optional[int] = Field(None, alias='724', description='')
    SubscriptionRequestType: Optional[str] = Field(None, alias='263', description='')
    TotalNumPosReports: Optional[int] = Field(None, alias='727', description='')
    UnsolicitedIndicator: Optional[bool] = Field(None, alias='325', description='')
    PosReqResult: int = Field(..., alias='728', description='')
    ClearingBusinessDate: date = Field(..., alias='715', description='')
    SettlSessID: Optional[str] = Field(None, alias='716', description='')
    SettlSessSubID: Optional[str] = Field(None, alias='717', description='')
    Account: str = Field(..., alias='1', description='')
    AcctIDSource: Optional[int] = Field(None, alias='660', description='')
    AccountType: int = Field(..., alias='581', description='')
    Currency: Optional[str] = Field(None, alias='15', description='')
    SettlPrice: float = Field(..., alias='730', description='')
    SettlPriceType: int = Field(..., alias='731', description='')
    PriorSettlPrice: float = Field(..., alias='734', description='')
    RegistStatus: Optional[str] = Field(None, alias='506', description='')
    DeliveryDate: Optional[date] = Field(None, alias='743', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    Parties: PartiesComponent = Field(..., description='')
    Instrument: Optional[InstrumentComponent] = Field(None, description='')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='')
    PosUndInstrmtGrp: Optional[PosUndInstrmtGrpComponent] = Field(None, description='')
    PositionQty: PositionQtyComponent = Field(..., description='')
    PositionAmountData: PositionAmountDataComponent = Field(..., description='')

