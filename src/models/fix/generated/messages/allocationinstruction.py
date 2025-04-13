from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.ordallocgrp import OrdAllocGrpComponent
from src.models.fix.generated.components.execallocgrp import ExecAllocGrpComponent
from src.models.fix.generated.components.instrument import InstrumentComponent
from src.models.fix.generated.components.instrumentextension import InstrumentExtensionComponent
from src.models.fix.generated.components.financingdetails import FinancingDetailsComponent
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrpComponent
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrpComponent
from src.models.fix.generated.components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveDataComponent
from src.models.fix.generated.components.parties import PartiesComponent
from src.models.fix.generated.components.stipulations import StipulationsComponent
from src.models.fix.generated.components.yielddata import YieldDataComponent
from src.models.fix.generated.components.allocgrp import AllocGrpComponent

class AllocationInstruction(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    AllocID: str = Field(..., description='', alias='70')
    AllocTransType: str = Field(..., description='', alias='71')
    AllocType: int = Field(..., description='', alias='626')
    SecondaryAllocID: Optional[str] = Field(None, description='', alias='793')
    RefAllocID: Optional[str] = Field(None, description='', alias='72')
    AllocCancReplaceReason: Optional[int] = Field(None, description='', alias='796')
    AllocIntermedReqType: Optional[int] = Field(None, description='', alias='808')
    AllocLinkID: Optional[str] = Field(None, description='', alias='196')
    AllocLinkType: Optional[int] = Field(None, description='', alias='197')
    BookingRefID: Optional[str] = Field(None, description='', alias='466')
    AllocNoOrdersType: int = Field(..., description='', alias='857')
    PreviouslyReported: Optional[bool] = Field(None, description='', alias='570')
    ReversalIndicator: Optional[bool] = Field(None, description='', alias='700')
    MatchType: Optional[str] = Field(None, description='', alias='574')
    Side: str = Field(..., description='', alias='54')
    Quantity: float = Field(..., description='', alias='53')
    QtyType: Optional[int] = Field(None, description='', alias='854')
    LastMkt: Optional[str] = Field(None, description='', alias='30')
    TradeOriginationDate: Optional[date] = Field(None, description='', alias='229')
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    PriceType: Optional[int] = Field(None, description='', alias='423')
    AvgPx: float = Field(..., description='', alias='6')
    AvgParPx: Optional[float] = Field(None, description='', alias='860')
    Currency: Optional[str] = Field(None, description='', alias='15')
    AvgPxPrecision: Optional[int] = Field(None, description='', alias='74')
    TradeDate: date = Field(..., description='', alias='75')
    TransactTime: Optional[datetime] = Field(None, description='', alias='60')
    SettlType: Optional[str] = Field(None, description='', alias='63')
    SettlDate: Optional[date] = Field(None, description='', alias='64')
    BookingType: Optional[int] = Field(None, description='', alias='775')
    GrossTradeAmt: Optional[float] = Field(None, description='', alias='381')
    Concession: Optional[float] = Field(None, description='', alias='238')
    TotalTakedown: Optional[float] = Field(None, description='', alias='237')
    NetMoney: Optional[float] = Field(None, description='', alias='118')
    PositionEffect: Optional[str] = Field(None, description='', alias='77')
    AutoAcceptIndicator: Optional[bool] = Field(None, description='', alias='754')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    NumDaysInterest: Optional[int] = Field(None, description='', alias='157')
    AccruedInterestRate: Optional[float] = Field(None, description='', alias='158')
    AccruedInterestAmt: Optional[float] = Field(None, description='', alias='159')
    TotalAccruedInterestAmt: Optional[float] = Field(None, description='', alias='540')
    InterestAtMaturity: Optional[float] = Field(None, description='', alias='738')
    EndAccruedInterestAmt: Optional[float] = Field(None, description='', alias='920')
    StartCash: Optional[float] = Field(None, description='', alias='921')
    EndCash: Optional[float] = Field(None, description='', alias='922')
    LegalConfirm: Optional[bool] = Field(None, description='', alias='650')
    TotNoAllocs: Optional[int] = Field(None, description='', alias='892')
    LastFragment: Optional[bool] = Field(None, description='', alias='893')
    OrdAllocGrp: Optional[OrdAllocGrpComponent] = Field(None, description='OrdAllocGrp component')
    ExecAllocGrp: Optional[ExecAllocGrpComponent] = Field(None, description='ExecAllocGrp component')
    Instrument: InstrumentComponent = Field(..., description='Instrument component')
    InstrumentExtension: Optional[InstrumentExtensionComponent] = Field(None, description='InstrumentExtension component')
    FinancingDetails: Optional[FinancingDetailsComponent] = Field(None, description='FinancingDetails component')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='UndInstrmtGrp component')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='InstrmtLegGrp component')
    SpreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveDataComponent] = Field(None, description='SpreadOrBenchmarkCurveData component')
    Parties: Optional[PartiesComponent] = Field(None, description='Parties component')
    Stipulations: Optional[StipulationsComponent] = Field(None, description='Stipulations component')
    YieldData: Optional[YieldDataComponent] = Field(None, description='YieldData component')
    AllocGrp: Optional[AllocGrpComponent] = Field(None, description='AllocGrp component')

