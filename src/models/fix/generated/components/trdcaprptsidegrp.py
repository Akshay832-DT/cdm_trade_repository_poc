"""
FIX 4.4 TrdCapRptSideGrp Component

This module contains the Pydantic model for the TrdCapRptSideGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.parties import Parties
from src.models.fix.generated.components.clrinstgrp import ClrInstGrp
from src.models.fix.generated.components.commissiondata import CommissionData
from src.models.fix.generated.components.contamtgrp import ContAmtGrp
from src.models.fix.generated.components.stipulations import Stipulations
from src.models.fix.generated.components.miscfeesgrp import MiscFeesGrp
from src.models.fix.generated.components.trdallocgrp import TrdAllocGrp


class NoSides(FIXMessageBase):
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
    
    side: str = Field(..., description='', alias='54')
    orderID: str = Field(..., description='', alias='37')
    secondaryOrderID: Optional[str] = Field(None, description='', alias='198')
    clOrdID: Optional[str] = Field(None, description='', alias='11')
    secondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    listID: Optional[str] = Field(None, description='', alias='66')
    account: Optional[str] = Field(None, description='', alias='1')
    acctIDSource: Optional[int] = Field(None, description='', alias='660')
    accountType: Optional[int] = Field(None, description='', alias='581')
    processCode: Optional[str] = Field(None, description='', alias='81')
    oddLot: Optional[bool] = Field(None, description='', alias='575')
    tradeInputSource: Optional[str] = Field(None, description='', alias='578')
    tradeInputDevice: Optional[str] = Field(None, description='', alias='579')
    orderInputDevice: Optional[str] = Field(None, description='', alias='821')
    currency: Optional[str] = Field(None, description='', alias='15')
    complianceID: Optional[str] = Field(None, description='', alias='376')
    solicitedFlag: Optional[bool] = Field(None, description='', alias='377')
    orderCapacity: Optional[str] = Field(None, description='', alias='528')
    orderRestrictions: Optional[List[str]] = Field(None, description='', alias='529')
    custOrderCapacity: Optional[int] = Field(None, description='', alias='582')
    ordType: Optional[str] = Field(None, description='', alias='40')
    execInst: Optional[List[str]] = Field(None, description='', alias='18')
    transBkdTime: Optional[datetime] = Field(None, description='', alias='483')
    tradingSessionID: Optional[str] = Field(None, description='', alias='336')
    tradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    timeBracket: Optional[str] = Field(None, description='', alias='943')
    grossTradeAmt: Optional[float] = Field(None, description='', alias='381')
    numDaysInterest: Optional[int] = Field(None, description='', alias='157')
    exDate: Optional[date] = Field(None, description='', alias='230')
    accruedInterestRate: Optional[float] = Field(None, description='', alias='158')
    accruedInterestAmt: Optional[float] = Field(None, description='', alias='159')
    interestAtMaturity: Optional[float] = Field(None, description='', alias='738')
    endAccruedInterestAmt: Optional[float] = Field(None, description='', alias='920')
    startCash: Optional[float] = Field(None, description='', alias='921')
    endCash: Optional[float] = Field(None, description='', alias='922')
    concession: Optional[float] = Field(None, description='', alias='238')
    totalTakedown: Optional[float] = Field(None, description='', alias='237')
    netMoney: Optional[float] = Field(None, description='', alias='118')
    settlCurrAmt: Optional[float] = Field(None, description='', alias='119')
    settlCurrency: Optional[str] = Field(None, description='', alias='120')
    settlCurrFxRate: Optional[float] = Field(None, description='', alias='155')
    settlCurrFxRateCalc: Optional[str] = Field(None, description='', alias='156')
    positionEffect: Optional[str] = Field(None, description='', alias='77')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')
    sideMultiLegReportingType: Optional[int] = Field(None, description='', alias='752')
    exchangeRule: Optional[str] = Field(None, description='', alias='825')
    tradeAllocIndicator: Optional[int] = Field(None, description='', alias='826')
    preallocMethod: Optional[str] = Field(None, description='', alias='591')
    allocID: Optional[str] = Field(None, description='', alias='70')


class TrdCapRptSideGrp(FIXMessageBase):
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
    
    parties: Optional[Parties] = Field(None, description='Parties component')
    clrInstGrp: Optional[ClrInstGrp] = Field(None, description='ClrInstGrp component')
    commissionData: Optional[CommissionData] = Field(None, description='CommissionData component')
    contAmtGrp: Optional[ContAmtGrp] = Field(None, description='ContAmtGrp component')
    stipulations: Optional[Stipulations] = Field(None, description='Stipulations component')
    miscFeesGrp: Optional[MiscFeesGrp] = Field(None, description='MiscFeesGrp component')
    trdAllocGrp: Optional[TrdAllocGrp] = Field(None, description='TrdAllocGrp component')
    noSides: Optional[int] = Field(None, description='Number of NoSides entries', alias='552')
    noSides_items: List[NoSides] = Field(default_factory=list)
