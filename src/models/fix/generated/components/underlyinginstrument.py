"""
FIX 4.4 UnderlyingInstrument Component

This module contains the Pydantic model for the UnderlyingInstrument component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class UnderlyingInstrument(FIXMessageBase):
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
    underlyingSymbol: Optional[str] = Field(None, description='', alias='311')
    underlyingSymbolSfx: Optional[str] = Field(None, description='', alias='312')
    underlyingSecurityID: Optional[str] = Field(None, description='', alias='309')
    underlyingSecurityIDSource: Optional[str] = Field(None, description='', alias='305')
    underlyingProduct: Optional[int] = Field(None, description='', alias='462')
    underlyingCFICode: Optional[str] = Field(None, description='', alias='463')
    underlyingSecurityType: Optional[str] = Field(None, description='', alias='310')
    underlyingSecuritySubType: Optional[str] = Field(None, description='', alias='763')
    underlyingMaturityMonthYear: Optional[str] = Field(None, description='', alias='313')
    underlyingMaturityDate: Optional[date] = Field(None, description='', alias='542')
    underlyingPutOrCall: Optional[int] = Field(None, description='', alias='315')
    underlyingCouponPaymentDate: Optional[date] = Field(None, description='', alias='241')
    underlyingIssueDate: Optional[date] = Field(None, description='', alias='242')
    underlyingRepoCollateralSecurityType: Optional[str] = Field(None, description='', alias='243')
    underlyingRepurchaseTerm: Optional[int] = Field(None, description='', alias='244')
    underlyingRepurchaseRate: Optional[float] = Field(None, description='', alias='245')
    underlyingFactor: Optional[float] = Field(None, description='', alias='246')
    underlyingCreditRating: Optional[str] = Field(None, description='', alias='256')
    underlyingInstrRegistry: Optional[str] = Field(None, description='', alias='595')
    underlyingCountryOfIssue: Optional[str] = Field(None, description='', alias='592')
    underlyingStateOrProvinceOfIssue: Optional[str] = Field(None, description='', alias='593')
    underlyingLocaleOfIssue: Optional[str] = Field(None, description='', alias='594')
    underlyingRedemptionDate: Optional[date] = Field(None, description='', alias='247')
    underlyingStrikePrice: Optional[float] = Field(None, description='', alias='316')
    underlyingStrikeCurrency: Optional[str] = Field(None, description='', alias='941')
    underlyingOptAttribute: Optional[str] = Field(None, description='', alias='317')
    underlyingContractMultiplier: Optional[float] = Field(None, description='', alias='436')
    underlyingCouponRate: Optional[float] = Field(None, description='', alias='435')
    underlyingSecurityExchange: Optional[str] = Field(None, description='', alias='308')
    underlyingIssuer: Optional[str] = Field(None, description='', alias='306')
    encodedUnderlyingIssuerLen: Optional[int] = Field(None, description='', alias='362')
    encodedUnderlyingIssuer: Optional[str] = Field(None, description='', alias='363')
    underlyingSecurityDesc: Optional[str] = Field(None, description='', alias='307')
    encodedUnderlyingSecurityDescLen: Optional[int] = Field(None, description='', alias='364')
    encodedUnderlyingSecurityDesc: Optional[str] = Field(None, description='', alias='365')
    underlyingCPProgram: Optional[str] = Field(None, description='', alias='877')
    underlyingCPRegType: Optional[str] = Field(None, description='', alias='878')
    underlyingCurrency: Optional[str] = Field(None, description='', alias='318')
    underlyingQty: Optional[float] = Field(None, description='', alias='879')
    underlyingPx: Optional[float] = Field(None, description='', alias='810')
    underlyingDirtyPrice: Optional[float] = Field(None, description='', alias='882')
    underlyingEndPrice: Optional[float] = Field(None, description='', alias='883')
    underlyingStartValue: Optional[float] = Field(None, description='', alias='884')
    underlyingCurrentValue: Optional[float] = Field(None, description='', alias='885')
    underlyingEndValue: Optional[float] = Field(None, description='', alias='886')
    undSecAltIDGrp: Optional[str] = Field(None)
    underlyingStipulations: Optional[str] = Field(None)
