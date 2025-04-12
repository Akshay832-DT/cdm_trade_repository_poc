"""
FIX 4.4 AllocationReport Message

This module contains the Pydantic model for the AllocationReport message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.allocgrp import AllocGrp
from src.models.fix.generated.components.execallocgrp import ExecAllocGrp
from src.models.fix.generated.components.financingdetails import FinancingDetails
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.instrumentextension import InstrumentExtension
from src.models.fix.generated.components.ordallocgrp import OrdAllocGrp
from src.models.fix.generated.components.parties import Parties
from src.models.fix.generated.components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveData
from src.models.fix.generated.components.stipulations import Stipulations
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp
from src.models.fix.generated.components.yielddata import YieldData


class AllocationReport(FIXMessageBase):
    """
    FIX 4.4 AllocationReport Message
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
    msgType: Literal["AS"] = Field("AS", alias='35')
    
    # Message-specific fields
    allocReportID: Optional[str] = Field(None, description='', alias='755')
    allocID: Optional[str] = Field(None, description='', alias='70')
    allocTransType: Optional[str] = Field(None, description='', alias='71')
    allocReportRefID: Optional[str] = Field(None, description='', alias='795')
    allocCancReplaceReason: Optional[int] = Field(None, description='', alias='796')
    secondaryAllocID: Optional[str] = Field(None, description='', alias='793')
    allocReportType: Optional[int] = Field(None, description='', alias='794')
    allocStatus: Optional[int] = Field(None, description='', alias='87')
    allocRejCode: Optional[int] = Field(None, description='', alias='88')
    refAllocID: Optional[str] = Field(None, description='', alias='72')
    allocIntermedReqType: Optional[int] = Field(None, description='', alias='808')
    allocLinkID: Optional[str] = Field(None, description='', alias='196')
    allocLinkType: Optional[int] = Field(None, description='', alias='197')
    bookingRefID: Optional[str] = Field(None, description='', alias='466')
    allocNoOrdersType: Optional[int] = Field(None, description='', alias='857')
    previouslyReported: Optional[bool] = Field(None, description='', alias='570')
    reversalIndicator: Optional[bool] = Field(None, description='', alias='700')
    matchType: Optional[str] = Field(None, description='', alias='574')
    side: Optional[str] = Field(None, description='', alias='54')
    quantity: Optional[float] = Field(None, description='', alias='53')
    qtyType: Optional[int] = Field(None, description='', alias='854')
    lastMkt: Optional[str] = Field(None, description='', alias='30')
    tradeOriginationDate: Optional[date] = Field(None, description='', alias='229')
    tradingSessionID: Optional[str] = Field(None, description='', alias='336')
    tradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    priceType: Optional[int] = Field(None, description='', alias='423')
    avgPx: Optional[float] = Field(None, description='', alias='6')
    avgParPx: Optional[float] = Field(None, description='', alias='860')
    currency: Optional[str] = Field(None, description='', alias='15')
    avgPxPrecision: Optional[int] = Field(None, description='', alias='74')
    tradeDate: Optional[date] = Field(None, description='', alias='75')
    transactTime: Optional[datetime] = Field(None, description='', alias='60')
    settlType: Optional[str] = Field(None, description='', alias='63')
    settlDate: Optional[date] = Field(None, description='', alias='64')
    bookingType: Optional[int] = Field(None, description='', alias='775')
    grossTradeAmt: Optional[float] = Field(None, description='', alias='381')
    concession: Optional[float] = Field(None, description='', alias='238')
    totalTakedown: Optional[float] = Field(None, description='', alias='237')
    netMoney: Optional[float] = Field(None, description='', alias='118')
    positionEffect: Optional[str] = Field(None, description='', alias='77')
    autoAcceptIndicator: Optional[bool] = Field(None, description='', alias='754')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')
    numDaysInterest: Optional[int] = Field(None, description='', alias='157')
    accruedInterestRate: Optional[float] = Field(None, description='', alias='158')
    accruedInterestAmt: Optional[float] = Field(None, description='', alias='159')
    totalAccruedInterestAmt: Optional[float] = Field(None, description='', alias='540')
    interestAtMaturity: Optional[float] = Field(None, description='', alias='738')
    endAccruedInterestAmt: Optional[float] = Field(None, description='', alias='920')
    startCash: Optional[float] = Field(None, description='', alias='921')
    endCash: Optional[float] = Field(None, description='', alias='922')
    legalConfirm: Optional[bool] = Field(None, description='', alias='650')
    totNoAllocs: Optional[int] = Field(None, description='', alias='892')
    lastFragment: Optional[bool] = Field(None, description='', alias='893')
    ordAllocGrp: Optional[OrdAllocGrp] = Field(None, description='OrdAllocGrp component')
    execAllocGrp: Optional[ExecAllocGrp] = Field(None, description='ExecAllocGrp component')
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    instrumentExtension: Optional[InstrumentExtension] = Field(None, description='InstrumentExtension component')
    financingDetails: Optional[FinancingDetails] = Field(None, description='FinancingDetails component')
    undInstrmtGrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    instrmtLegGrp: Optional[InstrmtLegGrp] = Field(None, description='InstrmtLegGrp component')
    spreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveData] = Field(None, description='SpreadOrBenchmarkCurveData component')
    parties: Optional[Parties] = Field(None, description='Parties component')
    stipulations: Optional[Stipulations] = Field(None, description='Stipulations component')
    yieldData: Optional[YieldData] = Field(None, description='YieldData component')
    allocGrp: Optional[AllocGrp] = Field(None, description='AllocGrp component')

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
