"""FIX message model for PositionMaintenanceReport (AM).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.instrmtleggrp import InstrmtLegGrpComponent
from ..components.instrument import InstrumentComponent
from ..components.parties import PartiesComponent
from ..components.positionamountdata import PositionAmountDataComponent
from ..components.positionqty import PositionQtyComponent
from ..components.trdgsesgrp import TrdgSesGrpComponent
from ..components.undinstrmtgrp import UndInstrmtGrpComponent

class PositionMaintenanceReportMessage(FIXMessageBase):
    """FIX message model for PositionMaintenanceReport."""

    MsgType: str = Field("AM", alias="35")

    PosMaintRptID: str = Field(..., alias='721', description='')
    PosTransType: int = Field(..., alias='709', description='')
    PosReqID: Optional[str] = Field(None, alias='710', description='')
    PosMaintAction: int = Field(..., alias='712', description='')
    OrigPosReqRefID: str = Field(..., alias='713', description='')
    PosMaintStatus: int = Field(..., alias='722', description='')
    PosMaintResult: Optional[int] = Field(None, alias='723', description='')
    ClearingBusinessDate: date = Field(..., alias='715', description='')
    SettlSessID: Optional[str] = Field(None, alias='716', description='')
    SettlSessSubID: Optional[str] = Field(None, alias='717', description='')
    Account: str = Field(..., alias='1', description='')
    AcctIDSource: Optional[int] = Field(None, alias='660', description='')
    AccountType: int = Field(..., alias='581', description='')
    Currency: Optional[str] = Field(None, alias='15', description='')
    TransactTime: datetime = Field(..., alias='60', description='')
    AdjustmentType: Optional[int] = Field(None, alias='718', description='')
    ThresholdAmount: Optional[float] = Field(None, alias='834', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    Parties: Optional[PartiesComponent] = Field(None, description='')
    Instrument: InstrumentComponent = Field(..., description='')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')
    TrdgSesGrp: Optional[TrdgSesGrpComponent] = Field(None, description='')
    PositionQty: PositionQtyComponent = Field(..., description='')
    PositionAmountData: PositionAmountDataComponent = Field(..., description='')

