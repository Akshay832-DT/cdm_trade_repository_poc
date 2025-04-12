"""
FIX 4.4 UnderlyingInstrument Component

This module contains the Pydantic model for the UnderlyingInstrument component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class UnderlyingInstrument(TradeModel):
    """
    FIX 4.4 UnderlyingInstrument Component
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
    UnderlyingSymbol: Optional[str] = Field(None, description='', alias='311')
    UnderlyingSymbolSfx: Optional[str] = Field(None, description='', alias='312')
    UnderlyingSecurityID: Optional[str] = Field(None, description='', alias='309')
    UnderlyingSecurityIDSource: Optional[str] = Field(None, description='', alias='305')
    UnderlyingProduct: Optional[int] = Field(None, description='', alias='462')
    UnderlyingCFICode: Optional[str] = Field(None, description='', alias='463')
    UnderlyingSecurityType: Optional[str] = Field(None, description='', alias='310')
    UnderlyingSecuritySubType: Optional[str] = Field(None, description='', alias='763')
    UnderlyingMaturityMonthYear: Optional[str] = Field(None, description='', alias='313')
    UnderlyingMaturityDate: Optional[date] = Field(None, description='', alias='542')
    UnderlyingPutOrCall: Optional[int] = Field(None, description='', alias='315')
    UnderlyingCouponPaymentDate: Optional[date] = Field(None, description='', alias='241')
    UnderlyingIssueDate: Optional[date] = Field(None, description='', alias='242')
    UnderlyingRepoCollateralSecurityType: Optional[str] = Field(None, description='', alias='243')
    UnderlyingRepurchaseTerm: Optional[int] = Field(None, description='', alias='244')
    UnderlyingRepurchaseRate: Optional[float] = Field(None, description='', alias='245')
    UnderlyingFactor: Optional[float] = Field(None, description='', alias='246')
    UnderlyingCreditRating: Optional[str] = Field(None, description='', alias='256')
    UnderlyingInstrRegistry: Optional[str] = Field(None, description='', alias='595')
    UnderlyingCountryOfIssue: Optional[str] = Field(None, description='', alias='592')
    UnderlyingStateOrProvinceOfIssue: Optional[str] = Field(None, description='', alias='593')
    UnderlyingLocaleOfIssue: Optional[str] = Field(None, description='', alias='594')
    UnderlyingRedemptionDate: Optional[date] = Field(None, description='', alias='247')
    UnderlyingStrikePrice: Optional[float] = Field(None, description='', alias='316')
    UnderlyingStrikeCurrency: Optional[str] = Field(None, description='', alias='941')
    UnderlyingOptAttribute: Optional[str] = Field(None, description='', alias='317')
    UnderlyingContractMultiplier: Optional[float] = Field(None, description='', alias='436')
    UnderlyingCouponRate: Optional[float] = Field(None, description='', alias='435')
    UnderlyingSecurityExchange: Optional[str] = Field(None, description='', alias='308')
    UnderlyingIssuer: Optional[str] = Field(None, description='', alias='306')
    EncodedUnderlyingIssuerLen: Optional[int] = Field(None, description='', alias='362')
    EncodedUnderlyingIssuer: Optional[str] = Field(None, description='', alias='363')
    UnderlyingSecurityDesc: Optional[str] = Field(None, description='', alias='307')
    EncodedUnderlyingSecurityDescLen: Optional[int] = Field(None, description='', alias='364')
    EncodedUnderlyingSecurityDesc: Optional[str] = Field(None, description='', alias='365')
    UnderlyingCPProgram: Optional[str] = Field(None, description='', alias='877')
    UnderlyingCPRegType: Optional[str] = Field(None, description='', alias='878')
    UnderlyingCurrency: Optional[str] = Field(None, description='', alias='318')
    UnderlyingQty: Optional[float] = Field(None, description='', alias='879')
    UnderlyingPx: Optional[float] = Field(None, description='', alias='810')
    UnderlyingDirtyPrice: Optional[float] = Field(None, description='', alias='882')
    UnderlyingEndPrice: Optional[float] = Field(None, description='', alias='883')
    UnderlyingStartValue: Optional[float] = Field(None, description='', alias='884')
    UnderlyingCurrentValue: Optional[float] = Field(None, description='', alias='885')
    UnderlyingEndValue: Optional[float] = Field(None, description='', alias='886')
    UndSecAltIDGrp: Optional[str] = Field(None)
    UnderlyingStipulations: Optional[str] = Field(None)
