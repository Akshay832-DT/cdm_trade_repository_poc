"""FIX message model for AllocationReport (AS).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.allocgrp import AllocGrpComponent
from ..components.execallocgrp import ExecAllocGrpComponent
from ..components.financingdetails import FinancingDetailsComponent
from ..components.instrmtleggrp import InstrmtLegGrpComponent
from ..components.instrument import InstrumentComponent
from ..components.instrumentextension import InstrumentExtensionComponent
from ..components.ordallocgrp import OrdAllocGrpComponent
from ..components.parties import PartiesComponent
from ..components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveDataComponent
from ..components.stipulations import StipulationsComponent
from ..components.undinstrmtgrp import UndInstrmtGrpComponent
from ..components.yielddata import YieldDataComponent

class AllocationReportMessage(FIXMessageBase):
    """FIX message model for AllocationReport."""

    MsgType: str = Field("AS", alias="35")

    AllocReportID: str = Field(..., alias='755', description='')
    AllocID: Optional[str] = Field(None, alias='70', description='')
    AllocTransType: str = Field(..., alias='71', description='')
    AllocReportRefID: Optional[str] = Field(None, alias='795', description='')
    AllocCancReplaceReason: Optional[int] = Field(None, alias='796', description='')
    SecondaryAllocID: Optional[str] = Field(None, alias='793', description='')
    AllocReportType: int = Field(..., alias='794', description='')
    AllocStatus: int = Field(..., alias='87', description='')
    AllocRejCode: Optional[int] = Field(None, alias='88', description='')
    RefAllocID: Optional[str] = Field(None, alias='72', description='')
    AllocIntermedReqType: Optional[int] = Field(None, alias='808', description='')
    AllocLinkID: Optional[str] = Field(None, alias='196', description='')
    AllocLinkType: Optional[int] = Field(None, alias='197', description='')
    BookingRefID: Optional[str] = Field(None, alias='466', description='')
    AllocNoOrdersType: int = Field(..., alias='857', description='')
    PreviouslyReported: Optional[bool] = Field(None, alias='570', description='')
    ReversalIndicator: Optional[bool] = Field(None, alias='700', description='')
    MatchType: Optional[str] = Field(None, alias='574', description='')
    Side: str = Field(..., alias='54', description='')
    Quantity: float = Field(..., alias='53', description='')
    QtyType: Optional[int] = Field(None, alias='854', description='')
    LastMkt: Optional[str] = Field(None, alias='30', description='')
    TradeOriginationDate: Optional[date] = Field(None, alias='229', description='')
    TradingSessionID: Optional[str] = Field(None, alias='336', description='')
    TradingSessionSubID: Optional[str] = Field(None, alias='625', description='')
    PriceType: Optional[int] = Field(None, alias='423', description='')
    AvgPx: float = Field(..., alias='6', description='')
    AvgParPx: Optional[float] = Field(None, alias='860', description='')
    Currency: Optional[str] = Field(None, alias='15', description='')
    AvgPxPrecision: Optional[int] = Field(None, alias='74', description='')
    TradeDate: date = Field(..., alias='75', description='')
    TransactTime: Optional[datetime] = Field(None, alias='60', description='')
    SettlType: Optional[str] = Field(None, alias='63', description='')
    SettlDate: Optional[date] = Field(None, alias='64', description='')
    BookingType: Optional[int] = Field(None, alias='775', description='')
    GrossTradeAmt: Optional[float] = Field(None, alias='381', description='')
    Concession: Optional[float] = Field(None, alias='238', description='')
    TotalTakedown: Optional[float] = Field(None, alias='237', description='')
    NetMoney: Optional[float] = Field(None, alias='118', description='')
    PositionEffect: Optional[str] = Field(None, alias='77', description='')
    AutoAcceptIndicator: Optional[bool] = Field(None, alias='754', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    NumDaysInterest: Optional[int] = Field(None, alias='157', description='')
    AccruedInterestRate: Optional[float] = Field(None, alias='158', description='')
    AccruedInterestAmt: Optional[float] = Field(None, alias='159', description='')
    TotalAccruedInterestAmt: Optional[float] = Field(None, alias='540', description='')
    InterestAtMaturity: Optional[float] = Field(None, alias='738', description='')
    EndAccruedInterestAmt: Optional[float] = Field(None, alias='920', description='')
    StartCash: Optional[float] = Field(None, alias='921', description='')
    EndCash: Optional[float] = Field(None, alias='922', description='')
    LegalConfirm: Optional[bool] = Field(None, alias='650', description='')
    TotNoAllocs: Optional[int] = Field(None, alias='892', description='')
    LastFragment: Optional[bool] = Field(None, alias='893', description='')
    OrdAllocGrp: Optional[OrdAllocGrpComponent] = Field(None, description='')
    ExecAllocGrp: Optional[ExecAllocGrpComponent] = Field(None, description='')
    Instrument: InstrumentComponent = Field(..., description='')
    InstrumentExtension: Optional[InstrumentExtensionComponent] = Field(None, description='')
    FinancingDetails: Optional[FinancingDetailsComponent] = Field(None, description='')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='')
    SpreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveDataComponent] = Field(None, description='')
    Parties: Optional[PartiesComponent] = Field(None, description='')
    Stipulations: Optional[StipulationsComponent] = Field(None, description='')
    YieldData: Optional[YieldDataComponent] = Field(None, description='')
    AllocGrp: Optional[AllocGrpComponent] = Field(None, description='')

