"""
FIX Component Model - TrdCapRptSideGrp
"""

from ..base import FIXComponentBase
from .clrinstgrp import ClrInstGrpComponent
from .commissiondata import CommissionDataComponent
from .contamtgrp import ContAmtGrpComponent
from .miscfeesgrp import MiscFeesGrpComponent
from .parties import PartiesComponent
from .stipulations import StipulationsComponent
from .trdallocgrp import TrdAllocGrpComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoSidesGroup(FIXComponentBase):

    """FIX Group - NoSides"""

    Side: str = Field(alias='54', description='')
    OrderID: str = Field(alias='37', description='')
    SecondaryOrderID: Optional[str] = Field(None, alias='198', description='')
    ClOrdID: Optional[str] = Field(None, alias='11', description='')
    SecondaryClOrdID: Optional[str] = Field(None, alias='526', description='')
    ListID: Optional[str] = Field(None, alias='66', description='')
    Account: Optional[str] = Field(None, alias='1', description='')
    AcctIDSource: Optional[int] = Field(None, alias='660', description='')
    AccountType: Optional[int] = Field(None, alias='581', description='')
    ProcessCode: Optional[str] = Field(None, alias='81', description='')
    OddLot: Optional[bool] = Field(None, alias='575', description='')
    TradeInputSource: Optional[str] = Field(None, alias='578', description='')
    TradeInputDevice: Optional[str] = Field(None, alias='579', description='')
    OrderInputDevice: Optional[str] = Field(None, alias='821', description='')
    Currency: Optional[str] = Field(None, alias='15', description='')
    ComplianceID: Optional[str] = Field(None, alias='376', description='')
    SolicitedFlag: Optional[bool] = Field(None, alias='377', description='')
    OrderCapacity: Optional[str] = Field(None, alias='528', description='')
    OrderRestrictions: Optional[str] = Field(None, alias='529', description='')
    CustOrderCapacity: Optional[int] = Field(None, alias='582', description='')
    OrdType: Optional[str] = Field(None, alias='40', description='')
    ExecInst: Optional[str] = Field(None, alias='18', description='')
    TransBkdTime: Optional[datetime] = Field(None, alias='483', description='')
    TradingSessionID: Optional[str] = Field(None, alias='336', description='')
    TradingSessionSubID: Optional[str] = Field(None, alias='625', description='')
    TimeBracket: Optional[str] = Field(None, alias='943', description='')
    GrossTradeAmt: Optional[float] = Field(None, alias='381', description='')
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
    NetMoney: Optional[float] = Field(None, alias='118', description='')
    SettlCurrAmt: Optional[float] = Field(None, alias='119', description='')
    SettlCurrency: Optional[str] = Field(None, alias='120', description='')
    SettlCurrFxRate: Optional[float] = Field(None, alias='155', description='')
    SettlCurrFxRateCalc: Optional[str] = Field(None, alias='156', description='')
    PositionEffect: Optional[str] = Field(None, alias='77', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    SideMultiLegReportingType: Optional[int] = Field(None, alias='752', description='')
    ExchangeRule: Optional[str] = Field(None, alias='825', description='')
    TradeAllocIndicator: Optional[int] = Field(None, alias='826', description='')
    PreallocMethod: Optional[str] = Field(None, alias='591', description='')
    AllocID: Optional[str] = Field(None, alias='70', description='')
    Parties: Optional[PartiesComponent] = Field(None, description='')
    ClrInstGrp: Optional[ClrInstGrpComponent] = Field(None, description='')
    CommissionData: Optional[CommissionDataComponent] = Field(None, description='')
    ContAmtGrp: Optional[ContAmtGrpComponent] = Field(None, description='')
    Stipulations: Optional[StipulationsComponent] = Field(None, description='')
    MiscFeesGrp: Optional[MiscFeesGrpComponent] = Field(None, description='')
    TrdAllocGrp: Optional[TrdAllocGrpComponent] = Field(None, description='')



class TrdCapRptSideGrpComponent(FIXComponentBase):
    """FIX Component - TrdCapRptSideGrp"""


