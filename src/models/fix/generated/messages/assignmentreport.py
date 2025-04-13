from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.parties import PartiesComponent
from src.models.fix.generated.components.instrument import InstrumentComponent
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrpComponent
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrpComponent
from src.models.fix.generated.components.positionqty import PositionQtyComponent
from src.models.fix.generated.components.positionamountdata import PositionAmountDataComponent

class AssignmentReport(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    AsgnRptID: str = Field(..., description='', alias='833')
    TotNumAssignmentReports: Optional[int] = Field(None, description='', alias='832')
    LastRptRequested: Optional[bool] = Field(None, description='', alias='912')
    Account: Optional[str] = Field(None, description='', alias='1')
    AccountType: int = Field(..., description='', alias='581')
    Currency: Optional[str] = Field(None, description='', alias='15')
    ThresholdAmount: Optional[float] = Field(None, description='', alias='834')
    SettlPrice: float = Field(..., description='', alias='730')
    SettlPriceType: int = Field(..., description='', alias='731')
    UnderlyingSettlPrice: float = Field(..., description='', alias='732')
    ExpireDate: Optional[date] = Field(None, description='', alias='432')
    AssignmentMethod: str = Field(..., description='', alias='744')
    AssignmentUnit: Optional[float] = Field(None, description='', alias='745')
    OpenInterest: float = Field(..., description='', alias='746')
    ExerciseMethod: str = Field(..., description='', alias='747')
    SettlSessID: str = Field(..., description='', alias='716')
    SettlSessSubID: str = Field(..., description='', alias='717')
    ClearingBusinessDate: date = Field(..., description='', alias='715')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    Parties: PartiesComponent = Field(..., description='Parties component')
    Instrument: Optional[InstrumentComponent] = Field(None, description='Instrument component')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='InstrmtLegGrp component')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='UndInstrmtGrp component')
    PositionQty: PositionQtyComponent = Field(..., description='PositionQty component')
    PositionAmountData: PositionAmountDataComponent = Field(..., description='PositionAmountData component')

