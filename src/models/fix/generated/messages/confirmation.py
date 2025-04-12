"""
FIX 4.4 Confirmation Message

This module contains the Pydantic model for the Confirmation message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.commissiondata import CommissionData
from src.models.fix.generated.components.cpctyconfgrp import CpctyConfGrp
from src.models.fix.generated.components.financingdetails import FinancingDetails
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.instrumentextension import InstrumentExtension
from src.models.fix.generated.components.miscfeesgrp import MiscFeesGrp
from src.models.fix.generated.components.ordallocgrp import OrdAllocGrp
from src.models.fix.generated.components.parties import Parties
from src.models.fix.generated.components.settlinstructionsdata import SettlInstructionsData
from src.models.fix.generated.components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveData
from src.models.fix.generated.components.stipulations import Stipulations
from src.models.fix.generated.components.trdregtimestamps import TrdRegTimestamps
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp
from src.models.fix.generated.components.yielddata import YieldData


class Confirmation(FIXMessageBase):
    """
    FIX 4.4 Confirmation Message
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
    
    # Set the message type for this message
    msgType: Literal["AK"] = Field("AK", alias='35')
    
    # Message-specific fields
    confirmID: Optional[str] = Field(None, description='', alias='664')
    confirmRefID: Optional[str] = Field(None, description='', alias='772')
    confirmReqID: Optional[str] = Field(None, description='', alias='859')
    confirmTransType: Optional[int] = Field(None, description='', alias='666')
    confirmType: Optional[int] = Field(None, description='', alias='773')
    copyMsgIndicator: Optional[bool] = Field(None, description='', alias='797')
    legalConfirm: Optional[bool] = Field(None, description='', alias='650')
    confirmStatus: Optional[int] = Field(None, description='', alias='665')
    allocID: Optional[str] = Field(None, description='', alias='70')
    secondaryAllocID: Optional[str] = Field(None, description='', alias='793')
    individualAllocID: Optional[str] = Field(None, description='', alias='467')
    transactTime: Optional[datetime] = Field(None, description='', alias='60')
    tradeDate: Optional[date] = Field(None, description='', alias='75')
    allocQty: Optional[float] = Field(None, description='', alias='80')
    qtyType: Optional[int] = Field(None, description='', alias='854')
    side: Optional[str] = Field(None, description='', alias='54')
    currency: Optional[str] = Field(None, description='', alias='15')
    lastMkt: Optional[str] = Field(None, description='', alias='30')
    allocAccount: Optional[str] = Field(None, description='', alias='79')
    allocAcctIDSource: Optional[int] = Field(None, description='', alias='661')
    allocAccountType: Optional[int] = Field(None, description='', alias='798')
    avgPx: Optional[float] = Field(None, description='', alias='6')
    avgPxPrecision: Optional[int] = Field(None, description='', alias='74')
    priceType: Optional[int] = Field(None, description='', alias='423')
    avgParPx: Optional[float] = Field(None, description='', alias='860')
    reportedPx: Optional[float] = Field(None, description='', alias='861')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')
    processCode: Optional[str] = Field(None, description='', alias='81')
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
    maturityNetMoney: Optional[float] = Field(None, description='', alias='890')
    settlCurrAmt: Optional[float] = Field(None, description='', alias='119')
    settlCurrency: Optional[str] = Field(None, description='', alias='120')
    settlCurrFxRate: Optional[float] = Field(None, description='', alias='155')
    settlCurrFxRateCalc: Optional[str] = Field(None, description='', alias='156')
    settlType: Optional[str] = Field(None, description='', alias='63')
    settlDate: Optional[date] = Field(None, description='', alias='64')
    sharedCommission: Optional[float] = Field(None, description='', alias='858')
    parties: Optional[Parties] = Field(None, description='Parties component')
    ordAllocGrp: Optional[OrdAllocGrp] = Field(None, description='OrdAllocGrp component')
    trdRegTimestamps: Optional[TrdRegTimestamps] = Field(None, description='TrdRegTimestamps component')
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    instrumentExtension: Optional[InstrumentExtension] = Field(None, description='InstrumentExtension component')
    financingDetails: Optional[FinancingDetails] = Field(None, description='FinancingDetails component')
    undInstrmtGrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    instrmtLegGrp: Optional[InstrmtLegGrp] = Field(None, description='InstrmtLegGrp component')
    yieldData: Optional[YieldData] = Field(None, description='YieldData component')
    cpctyConfGrp: Optional[CpctyConfGrp] = Field(None, description='CpctyConfGrp component')
    spreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveData] = Field(None, description='SpreadOrBenchmarkCurveData component')
    settlInstructionsData: Optional[SettlInstructionsData] = Field(None, description='SettlInstructionsData component')
    commissionData: Optional[CommissionData] = Field(None, description='CommissionData component')
    stipulations: Optional[Stipulations] = Field(None, description='Stipulations component')
    miscFeesGrp: Optional[MiscFeesGrp] = Field(None, description='MiscFeesGrp component')

    def model_dump(self, **kwargs) -> Dict[str, Any]:
        """Override model_dump to handle nested components"""
        kwargs.setdefault('by_alias', True)
        data = super().model_dump(**kwargs)
        
        # Handle repeating components
        for field_name, value in data.items():
            if isinstance(value, list):
                # Set the No* field based on list length
                no_field = f"no{field_name}"  # Convert to camelCase
                if hasattr(self, no_field):
                    setattr(self, no_field, len(value))
        
        return data
