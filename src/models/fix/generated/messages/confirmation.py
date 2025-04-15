"""FIX message model for Confirmation (AK).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.commissiondata import CommissionDataComponent
from ..components.cpctyconfgrp import CpctyConfGrpComponent
from ..components.financingdetails import FinancingDetailsComponent
from ..components.instrmtleggrp import InstrmtLegGrpComponent
from ..components.instrument import InstrumentComponent
from ..components.instrumentextension import InstrumentExtensionComponent
from ..components.miscfeesgrp import MiscFeesGrpComponent
from ..components.ordallocgrp import OrdAllocGrpComponent
from ..components.parties import PartiesComponent
from ..components.settlinstructionsdata import SettlInstructionsDataComponent
from ..components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveDataComponent
from ..components.stipulations import StipulationsComponent
from ..components.trdregtimestamps import TrdRegTimestampsComponent
from ..components.undinstrmtgrp import UndInstrmtGrpComponent
from ..components.yielddata import YieldDataComponent

class ConfirmationMessage(FIXMessageBase):
    """FIX message model for Confirmation."""

    MsgType: str = Field("AK", alias="35")

    ConfirmID: str = Field(..., alias='664', description='')
    ConfirmRefID: Optional[str] = Field(None, alias='772', description='')
    ConfirmReqID: Optional[str] = Field(None, alias='859', description='')
    ConfirmTransType: int = Field(..., alias='666', description='')
    ConfirmType: int = Field(..., alias='773', description='')
    CopyMsgIndicator: Optional[bool] = Field(None, alias='797', description='')
    LegalConfirm: Optional[bool] = Field(None, alias='650', description='')
    ConfirmStatus: int = Field(..., alias='665', description='')
    AllocID: Optional[str] = Field(None, alias='70', description='')
    SecondaryAllocID: Optional[str] = Field(None, alias='793', description='')
    IndividualAllocID: Optional[str] = Field(None, alias='467', description='')
    TransactTime: datetime = Field(..., alias='60', description='')
    TradeDate: date = Field(..., alias='75', description='')
    AllocQty: float = Field(..., alias='80', description='')
    QtyType: Optional[int] = Field(None, alias='854', description='')
    Side: str = Field(..., alias='54', description='')
    Currency: Optional[str] = Field(None, alias='15', description='')
    LastMkt: Optional[str] = Field(None, alias='30', description='')
    AllocAccount: str = Field(..., alias='79', description='')
    AllocAcctIDSource: Optional[int] = Field(None, alias='661', description='')
    AllocAccountType: Optional[int] = Field(None, alias='798', description='')
    AvgPx: float = Field(..., alias='6', description='')
    AvgPxPrecision: Optional[int] = Field(None, alias='74', description='')
    PriceType: Optional[int] = Field(None, alias='423', description='')
    AvgParPx: Optional[float] = Field(None, alias='860', description='')
    ReportedPx: Optional[float] = Field(None, alias='861', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    ProcessCode: Optional[str] = Field(None, alias='81', description='')
    GrossTradeAmt: float = Field(..., alias='381', description='')
    NumDaysInterest: Optional[int] = Field(None, alias='157', description='')
    ExDate: Optional[date] = Field(None, alias='230', description='')
    AccruedInterestRate: Optional[float] = Field(None, alias='158', description='')
    AccruedInterestAmt: Optional[float] = Field(None, alias='159', description='')
    InterestAtMaturity: Optional[float] = Field(None, alias='738', description='')
    EndAccruedInterestAmt: Optional[float] = Field(None, alias='920', description='')
    StartCash: Optional[float] = Field(None, alias='921', description='')
    EndCash: Optional[float] = Field(None, alias='922', description='')
    Concession: Optional[float] = Field(None, alias='238', description='')
    TotalTakedown: Optional[float] = Field(None, alias='237', description='')
    NetMoney: float = Field(..., alias='118', description='')
    MaturityNetMoney: Optional[float] = Field(None, alias='890', description='')
    SettlCurrAmt: Optional[float] = Field(None, alias='119', description='')
    SettlCurrency: Optional[str] = Field(None, alias='120', description='')
    SettlCurrFxRate: Optional[float] = Field(None, alias='155', description='')
    SettlCurrFxRateCalc: Optional[str] = Field(None, alias='156', description='')
    SettlType: Optional[str] = Field(None, alias='63', description='')
    SettlDate: Optional[date] = Field(None, alias='64', description='')
    SharedCommission: Optional[float] = Field(None, alias='858', description='')
    Parties: Optional[PartiesComponent] = Field(None, description='')
    OrdAllocGrp: Optional[OrdAllocGrpComponent] = Field(None, description='')
    TrdRegTimestamps: Optional[TrdRegTimestampsComponent] = Field(None, description='')
    Instrument: InstrumentComponent = Field(..., description='')
    InstrumentExtension: Optional[InstrumentExtensionComponent] = Field(None, description='')
    FinancingDetails: Optional[FinancingDetailsComponent] = Field(None, description='')
    UndInstrmtGrp: UndInstrmtGrpComponent = Field(..., description='')
    InstrmtLegGrp: InstrmtLegGrpComponent = Field(..., description='')
    YieldData: Optional[YieldDataComponent] = Field(None, description='')
    CpctyConfGrp: CpctyConfGrpComponent = Field(..., description='')
    SpreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveDataComponent] = Field(None, description='')
    SettlInstructionsData: Optional[SettlInstructionsDataComponent] = Field(None, description='')
    CommissionData: Optional[CommissionDataComponent] = Field(None, description='')
    Stipulations: Optional[StipulationsComponent] = Field(None, description='')
    MiscFeesGrp: Optional[MiscFeesGrpComponent] = Field(None, description='')

