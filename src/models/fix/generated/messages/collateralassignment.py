from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.parties import PartiesComponent
from src.models.fix.generated.components.execcollgrp import ExecCollGrpComponent
from src.models.fix.generated.components.trdcollgrp import TrdCollGrpComponent
from src.models.fix.generated.components.instrument import InstrumentComponent
from src.models.fix.generated.components.financingdetails import FinancingDetailsComponent
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrpComponent
from src.models.fix.generated.components.undinstrmtcollgrp import UndInstrmtCollGrpComponent
from src.models.fix.generated.components.trdregtimestamps import TrdRegTimestampsComponent
from src.models.fix.generated.components.miscfeesgrp import MiscFeesGrpComponent
from src.models.fix.generated.components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveDataComponent
from src.models.fix.generated.components.stipulations import StipulationsComponent
from src.models.fix.generated.components.settlinstructionsdata import SettlInstructionsDataComponent

class CollateralAssignment(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    CollAsgnID: str = Field(..., description='', alias='902')
    CollReqID: Optional[str] = Field(None, description='', alias='894')
    CollAsgnReason: int = Field(..., description='', alias='895')
    CollAsgnTransType: int = Field(..., description='', alias='903')
    CollAsgnRefID: Optional[str] = Field(None, description='', alias='907')
    TransactTime: datetime = Field(..., description='', alias='60')
    ExpireTime: Optional[datetime] = Field(None, description='', alias='126')
    Account: Optional[str] = Field(None, description='', alias='1')
    AccountType: Optional[int] = Field(None, description='', alias='581')
    ClOrdID: Optional[str] = Field(None, description='', alias='11')
    OrderID: Optional[str] = Field(None, description='', alias='37')
    SecondaryOrderID: Optional[str] = Field(None, description='', alias='198')
    SecondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    SettlDate: Optional[date] = Field(None, description='', alias='64')
    Quantity: Optional[float] = Field(None, description='', alias='53')
    QtyType: Optional[int] = Field(None, description='', alias='854')
    Currency: Optional[str] = Field(None, description='', alias='15')
    MarginExcess: Optional[float] = Field(None, description='', alias='899')
    TotalNetValue: Optional[float] = Field(None, description='', alias='900')
    CashOutstanding: Optional[float] = Field(None, description='', alias='901')
    Side: Optional[str] = Field(None, description='', alias='54')
    Price: Optional[float] = Field(None, description='', alias='44')
    PriceType: Optional[int] = Field(None, description='', alias='423')
    AccruedInterestAmt: Optional[float] = Field(None, description='', alias='159')
    EndAccruedInterestAmt: Optional[float] = Field(None, description='', alias='920')
    StartCash: Optional[float] = Field(None, description='', alias='921')
    EndCash: Optional[float] = Field(None, description='', alias='922')
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    SettlSessID: Optional[str] = Field(None, description='', alias='716')
    SettlSessSubID: Optional[str] = Field(None, description='', alias='717')
    ClearingBusinessDate: Optional[date] = Field(None, description='', alias='715')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    Parties: Optional[PartiesComponent] = Field(None, description='Parties component')
    ExecCollGrp: Optional[ExecCollGrpComponent] = Field(None, description='ExecCollGrp component')
    TrdCollGrp: Optional[TrdCollGrpComponent] = Field(None, description='TrdCollGrp component')
    Instrument: Optional[InstrumentComponent] = Field(None, description='Instrument component')
    FinancingDetails: Optional[FinancingDetailsComponent] = Field(None, description='FinancingDetails component')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='InstrmtLegGrp component')
    UndInstrmtCollGrp: Optional[UndInstrmtCollGrpComponent] = Field(None, description='UndInstrmtCollGrp component')
    TrdRegTimestamps: Optional[TrdRegTimestampsComponent] = Field(None, description='TrdRegTimestamps component')
    MiscFeesGrp: Optional[MiscFeesGrpComponent] = Field(None, description='MiscFeesGrp component')
    SpreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveDataComponent] = Field(None, description='SpreadOrBenchmarkCurveData component')
    Stipulations: Optional[StipulationsComponent] = Field(None, description='Stipulations component')
    SettlInstructionsData: Optional[SettlInstructionsDataComponent] = Field(None, description='SettlInstructionsData component')

