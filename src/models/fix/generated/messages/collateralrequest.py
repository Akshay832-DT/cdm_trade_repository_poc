"""FIX message model for CollateralRequest (AX).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.execcollgrp import ExecCollGrpComponent
from ..components.financingdetails import FinancingDetailsComponent
from ..components.instrmtleggrp import InstrmtLegGrpComponent
from ..components.instrument import InstrumentComponent
from ..components.miscfeesgrp import MiscFeesGrpComponent
from ..components.parties import PartiesComponent
from ..components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveDataComponent
from ..components.stipulations import StipulationsComponent
from ..components.trdcollgrp import TrdCollGrpComponent
from ..components.trdregtimestamps import TrdRegTimestampsComponent
from ..components.undinstrmtcollgrp import UndInstrmtCollGrpComponent

class CollateralRequestMessage(FIXMessageBase):
    """FIX message model for CollateralRequest."""

    MsgType: str = Field("AX", alias="35")

    CollReqID: str = Field(..., alias='894', description='')
    CollAsgnReason: int = Field(..., alias='895', description='')
    TransactTime: datetime = Field(..., alias='60', description='')
    ExpireTime: Optional[datetime] = Field(None, alias='126', description='')
    Account: Optional[str] = Field(None, alias='1', description='')
    AccountType: Optional[int] = Field(None, alias='581', description='')
    ClOrdID: Optional[str] = Field(None, alias='11', description='')
    OrderID: Optional[str] = Field(None, alias='37', description='')
    SecondaryOrderID: Optional[str] = Field(None, alias='198', description='')
    SecondaryClOrdID: Optional[str] = Field(None, alias='526', description='')
    SettlDate: Optional[date] = Field(None, alias='64', description='')
    Quantity: Optional[float] = Field(None, alias='53', description='')
    QtyType: Optional[int] = Field(None, alias='854', description='')
    Currency: Optional[str] = Field(None, alias='15', description='')
    MarginExcess: Optional[float] = Field(None, alias='899', description='')
    TotalNetValue: Optional[float] = Field(None, alias='900', description='')
    CashOutstanding: Optional[float] = Field(None, alias='901', description='')
    Side: Optional[str] = Field(None, alias='54', description='')
    Price: Optional[float] = Field(None, alias='44', description='')
    PriceType: Optional[int] = Field(None, alias='423', description='')
    AccruedInterestAmt: Optional[float] = Field(None, alias='159', description='')
    EndAccruedInterestAmt: Optional[float] = Field(None, alias='920', description='')
    StartCash: Optional[float] = Field(None, alias='921', description='')
    EndCash: Optional[float] = Field(None, alias='922', description='')
    TradingSessionID: Optional[str] = Field(None, alias='336', description='')
    TradingSessionSubID: Optional[str] = Field(None, alias='625', description='')
    SettlSessID: Optional[str] = Field(None, alias='716', description='')
    SettlSessSubID: Optional[str] = Field(None, alias='717', description='')
    ClearingBusinessDate: Optional[date] = Field(None, alias='715', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    Parties: Optional[PartiesComponent] = Field(None, description='')
    ExecCollGrp: Optional[ExecCollGrpComponent] = Field(None, description='')
    TrdCollGrp: Optional[TrdCollGrpComponent] = Field(None, description='')
    Instrument: Optional[InstrumentComponent] = Field(None, description='')
    FinancingDetails: Optional[FinancingDetailsComponent] = Field(None, description='')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='')
    UndInstrmtCollGrp: Optional[UndInstrmtCollGrpComponent] = Field(None, description='')
    TrdRegTimestamps: Optional[TrdRegTimestampsComponent] = Field(None, description='')
    MiscFeesGrp: Optional[MiscFeesGrpComponent] = Field(None, description='')
    SpreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveDataComponent] = Field(None, description='')
    Stipulations: Optional[StipulationsComponent] = Field(None, description='')

