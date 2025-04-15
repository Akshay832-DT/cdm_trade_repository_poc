"""FIX message model for AssignmentReport (AW).

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
from ..components.undinstrmtgrp import UndInstrmtGrpComponent

class AssignmentReportMessage(FIXMessageBase):
    """FIX message model for AssignmentReport."""

    MsgType: str = Field("AW", alias="35")

    AsgnRptID: str = Field(..., alias='833', description='')
    TotNumAssignmentReports: Optional[int] = Field(None, alias='832', description='')
    LastRptRequested: Optional[bool] = Field(None, alias='912', description='')
    Account: Optional[str] = Field(None, alias='1', description='')
    AccountType: int = Field(..., alias='581', description='')
    Currency: Optional[str] = Field(None, alias='15', description='')
    ThresholdAmount: Optional[float] = Field(None, alias='834', description='')
    SettlPrice: float = Field(..., alias='730', description='')
    SettlPriceType: int = Field(..., alias='731', description='')
    UnderlyingSettlPrice: float = Field(..., alias='732', description='')
    ExpireDate: Optional[date] = Field(None, alias='432', description='')
    AssignmentMethod: str = Field(..., alias='744', description='')
    AssignmentUnit: Optional[float] = Field(None, alias='745', description='')
    OpenInterest: float = Field(..., alias='746', description='')
    ExerciseMethod: str = Field(..., alias='747', description='')
    SettlSessID: str = Field(..., alias='716', description='')
    SettlSessSubID: str = Field(..., alias='717', description='')
    ClearingBusinessDate: date = Field(..., alias='715', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    Parties: PartiesComponent = Field(..., description='')
    Instrument: Optional[InstrumentComponent] = Field(None, description='')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')
    PositionQty: PositionQtyComponent = Field(..., description='')
    PositionAmountData: PositionAmountDataComponent = Field(..., description='')

