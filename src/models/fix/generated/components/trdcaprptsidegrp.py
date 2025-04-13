"""
FIX 4.4 TrdCapRptSideGrp Component

This module contains the Pydantic model for the TrdCapRptSideGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoSidesGroup(FIXComponentBase):
    """
    NoSides group fields
    """
    model_config = ConfigDict(
        populate_by_name=True,
        validate_by_name=True,
        json_encoders={
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
            time: lambda v: v.isoformat()
        }
    )
    
    Side: str = Field(..., description='', alias='54')
    OrderID: str = Field(..., description='', alias='37')
    SecondaryOrderID: Optional[str] = Field(None, description='', alias='198')
    ClOrdID: Optional[str] = Field(None, description='', alias='11')
    SecondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    ListID: Optional[str] = Field(None, description='', alias='66')
    Account: Optional[str] = Field(None, description='', alias='1')
    AcctIDSource: Optional[int] = Field(None, description='', alias='660')
    AccountType: Optional[int] = Field(None, description='', alias='581')
    ProcessCode: Optional[str] = Field(None, description='', alias='81')
    OddLot: Optional[bool] = Field(None, description='', alias='575')
    TradeInputSource: Optional[str] = Field(None, description='', alias='578')
    TradeInputDevice: Optional[str] = Field(None, description='', alias='579')
    OrderInputDevice: Optional[str] = Field(None, description='', alias='821')
    Currency: Optional[str] = Field(None, description='', alias='15')
    ComplianceID: Optional[str] = Field(None, description='', alias='376')
    SolicitedFlag: Optional[bool] = Field(None, description='', alias='377')
    OrderCapacity: Optional[str] = Field(None, description='', alias='528')
    OrderRestrictions: Optional[List[str]] = Field(None, description='', alias='529')
    CustOrderCapacity: Optional[int] = Field(None, description='', alias='582')
    OrdType: Optional[str] = Field(None, description='', alias='40')
    ExecInst: Optional[List[str]] = Field(None, description='', alias='18')
    TransBkdTime: Optional[datetime] = Field(None, description='', alias='483')
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    TimeBracket: Optional[str] = Field(None, description='', alias='943')
    GrossTradeAmt: Optional[float] = Field(None, description='', alias='381')
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
    NetMoney: Optional[float] = Field(None, description='', alias='118')
    SettlCurrAmt: Optional[float] = Field(None, description='', alias='119')
    SettlCurrency: Optional[str] = Field(None, description='', alias='120')
    SettlCurrFxRate: Optional[float] = Field(None, description='', alias='155')
    SettlCurrFxRateCalc: Optional[str] = Field(None, description='', alias='156')
    PositionEffect: Optional[str] = Field(None, description='', alias='77')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    SideMultiLegReportingType: Optional[int] = Field(None, description='', alias='752')
    ExchangeRule: Optional[str] = Field(None, description='', alias='825')
    TradeAllocIndicator: Optional[int] = Field(None, description='', alias='826')
    PreallocMethod: Optional[str] = Field(None, description='', alias='591')
    AllocID: Optional[str] = Field(None, description='', alias='70')


class TrdCapRptSideGrpComponent(FIXComponentBase):
    """
    FIX 4.4 TrdCapRptSideGrp Component
    """
    model_config = ConfigDict(
        populate_by_name=True,
        validate_by_name=True,
        json_encoders={
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
            time: lambda v: v.isoformat()
        }
    )
    
    Parties: Optional[PartiesComponent] = Field(None, description='Parties component')
    ClrInstGrp: Optional[ClrInstGrpComponent] = Field(None, description='ClrInstGrp component')
    CommissionData: Optional[CommissionDataComponent] = Field(None, description='CommissionData component')
    ContAmtGrp: Optional[ContAmtGrpComponent] = Field(None, description='ContAmtGrp component')
    Stipulations: Optional[StipulationsComponent] = Field(None, description='Stipulations component')
    MiscFeesGrp: Optional[MiscFeesGrpComponent] = Field(None, description='MiscFeesGrp component')
    TrdAllocGrp: Optional[TrdAllocGrpComponent] = Field(None, description='TrdAllocGrp component')
    NoSides: Optional[int] = Field(None, description='Number of NoSides entries', alias='')
    NoSides_items: List[NoSidesGroup] = Field(default_factory=list)
