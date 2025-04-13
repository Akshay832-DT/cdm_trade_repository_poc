from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.parties import PartiesComponent
from src.models.fix.generated.components.ordallocgrp import OrdAllocGrpComponent
from src.models.fix.generated.components.trdregtimestamps import TrdRegTimestampsComponent
from src.models.fix.generated.components.instrument import InstrumentComponent
from src.models.fix.generated.components.instrumentextension import InstrumentExtensionComponent
from src.models.fix.generated.components.financingdetails import FinancingDetailsComponent
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrpComponent
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrpComponent
from src.models.fix.generated.components.yielddata import YieldDataComponent
from src.models.fix.generated.components.cpctyconfgrp import CpctyConfGrpComponent
from src.models.fix.generated.components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveDataComponent
from src.models.fix.generated.components.settlinstructionsdata import SettlInstructionsDataComponent
from src.models.fix.generated.components.commissiondata import CommissionDataComponent
from src.models.fix.generated.components.stipulations import StipulationsComponent
from src.models.fix.generated.components.miscfeesgrp import MiscFeesGrpComponent

class Confirmation(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    ConfirmID: str = Field(..., description='', alias='664')
    ConfirmRefID: Optional[str] = Field(None, description='', alias='772')
    ConfirmReqID: Optional[str] = Field(None, description='', alias='859')
    ConfirmTransType: int = Field(..., description='', alias='666')
    ConfirmType: int = Field(..., description='', alias='773')
    CopyMsgIndicator: Optional[bool] = Field(None, description='', alias='797')
    LegalConfirm: Optional[bool] = Field(None, description='', alias='650')
    ConfirmStatus: int = Field(..., description='', alias='665')
    AllocID: Optional[str] = Field(None, description='', alias='70')
    SecondaryAllocID: Optional[str] = Field(None, description='', alias='793')
    IndividualAllocID: Optional[str] = Field(None, description='', alias='467')
    TransactTime: datetime = Field(..., description='', alias='60')
    TradeDate: date = Field(..., description='', alias='75')
    AllocQty: float = Field(..., description='', alias='80')
    QtyType: Optional[int] = Field(None, description='', alias='854')
    Side: str = Field(..., description='', alias='54')
    Currency: Optional[str] = Field(None, description='', alias='15')
    LastMkt: Optional[str] = Field(None, description='', alias='30')
    AllocAccount: str = Field(..., description='', alias='79')
    AllocAcctIDSource: Optional[int] = Field(None, description='', alias='661')
    AllocAccountType: Optional[int] = Field(None, description='', alias='798')
    AvgPx: float = Field(..., description='', alias='6')
    AvgPxPrecision: Optional[int] = Field(None, description='', alias='74')
    PriceType: Optional[int] = Field(None, description='', alias='423')
    AvgParPx: Optional[float] = Field(None, description='', alias='860')
    ReportedPx: Optional[float] = Field(None, description='', alias='861')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    ProcessCode: Optional[str] = Field(None, description='', alias='81')
    GrossTradeAmt: float = Field(..., description='', alias='381')
    NumDaysInterest: Optional[int] = Field(None, description='', alias='157')
    ExDate: Optional[date] = Field(None, description='', alias='230')
    AccruedInterestRate: Optional[float] = Field(None, description='', alias='158')
    AccruedInterestAmt: Optional[float] = Field(None, description='', alias='159')
    InterestAtMaturity: Optional[float] = Field(None, description='', alias='738')
    EndAccruedInterestAmt: Optional[float] = Field(None, description='', alias='920')
    StartCash: Optional[float] = Field(None, description='', alias='921')
    EndCash: Optional[float] = Field(None, description='', alias='922')
    Concession: Optional[float] = Field(None, description='', alias='238')
    TotalTakedown: Optional[float] = Field(None, description='', alias='237')
    NetMoney: float = Field(..., description='', alias='118')
    MaturityNetMoney: Optional[float] = Field(None, description='', alias='890')
    SettlCurrAmt: Optional[float] = Field(None, description='', alias='119')
    SettlCurrency: Optional[str] = Field(None, description='', alias='120')
    SettlCurrFxRate: Optional[float] = Field(None, description='', alias='155')
    SettlCurrFxRateCalc: Optional[str] = Field(None, description='', alias='156')
    SettlType: Optional[str] = Field(None, description='', alias='63')
    SettlDate: Optional[date] = Field(None, description='', alias='64')
    SharedCommission: Optional[float] = Field(None, description='', alias='858')
    Parties: Optional[PartiesComponent] = Field(None, description='Parties component')
    OrdAllocGrp: Optional[OrdAllocGrpComponent] = Field(None, description='OrdAllocGrp component')
    TrdRegTimestamps: Optional[TrdRegTimestampsComponent] = Field(None, description='TrdRegTimestamps component')
    Instrument: InstrumentComponent = Field(..., description='Instrument component')
    InstrumentExtension: Optional[InstrumentExtensionComponent] = Field(None, description='InstrumentExtension component')
    FinancingDetails: Optional[FinancingDetailsComponent] = Field(None, description='FinancingDetails component')
    UndInstrmtGrp: UndInstrmtGrpComponent = Field(..., description='UndInstrmtGrp component')
    InstrmtLegGrp: InstrmtLegGrpComponent = Field(..., description='InstrmtLegGrp component')
    YieldData: Optional[YieldDataComponent] = Field(None, description='YieldData component')
    CpctyConfGrp: CpctyConfGrpComponent = Field(..., description='CpctyConfGrp component')
    SpreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveDataComponent] = Field(None, description='SpreadOrBenchmarkCurveData component')
    SettlInstructionsData: Optional[SettlInstructionsDataComponent] = Field(None, description='SettlInstructionsData component')
    CommissionData: Optional[CommissionDataComponent] = Field(None, description='CommissionData component')
    Stipulations: Optional[StipulationsComponent] = Field(None, description='Stipulations component')
    MiscFeesGrp: Optional[MiscFeesGrpComponent] = Field(None, description='MiscFeesGrp component')

