"""
FIX 4.4 Instrument Component

This module contains the Pydantic model for the Instrument component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class Instrument(TradeModel):
    """
    FIX 4.4 Instrument Component
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
    Symbol: Optional[str] = Field(None, description='', alias='55')
    SymbolSfx: Optional[str] = Field(None, description='', alias='65')
    SecurityID: Optional[str] = Field(None, description='', alias='48')
    SecurityIDSource: Optional[str] = Field(None, description='', alias='22')
    Product: Optional[int] = Field(None, description='', alias='460')
    CFICode: Optional[str] = Field(None, description='', alias='461')
    SecurityType: Optional[str] = Field(None, description='', alias='167')
    SecuritySubType: Optional[str] = Field(None, description='', alias='762')
    MaturityMonthYear: Optional[str] = Field(None, description='', alias='200')
    MaturityDate: Optional[date] = Field(None, description='', alias='541')
    PutOrCall: Optional[int] = Field(None, description='', alias='201')
    CouponPaymentDate: Optional[date] = Field(None, description='', alias='224')
    IssueDate: Optional[date] = Field(None, description='', alias='225')
    RepoCollateralSecurityType: Optional[str] = Field(None, description='', alias='239')
    RepurchaseTerm: Optional[int] = Field(None, description='', alias='226')
    RepurchaseRate: Optional[float] = Field(None, description='', alias='227')
    Factor: Optional[float] = Field(None, description='', alias='228')
    CreditRating: Optional[str] = Field(None, description='', alias='255')
    InstrRegistry: Optional[str] = Field(None, description='', alias='543')
    CountryOfIssue: Optional[str] = Field(None, description='', alias='470')
    StateOrProvinceOfIssue: Optional[str] = Field(None, description='', alias='471')
    LocaleOfIssue: Optional[str] = Field(None, description='', alias='472')
    RedemptionDate: Optional[date] = Field(None, description='', alias='240')
    StrikePrice: Optional[float] = Field(None, description='', alias='202')
    StrikeCurrency: Optional[str] = Field(None, description='', alias='947')
    OptAttribute: Optional[str] = Field(None, description='', alias='206')
    ContractMultiplier: Optional[float] = Field(None, description='', alias='231')
    CouponRate: Optional[float] = Field(None, description='', alias='223')
    SecurityExchange: Optional[str] = Field(None, description='', alias='207')
    Issuer: Optional[str] = Field(None, description='', alias='106')
    EncodedIssuerLen: Optional[int] = Field(None, description='', alias='348')
    EncodedIssuer: Optional[str] = Field(None, description='', alias='349')
    SecurityDesc: Optional[str] = Field(None, description='', alias='107')
    EncodedSecurityDescLen: Optional[int] = Field(None, description='', alias='350')
    EncodedSecurityDesc: Optional[str] = Field(None, description='', alias='351')
    Pool: Optional[str] = Field(None, description='', alias='691')
    ContractSettlMonth: Optional[str] = Field(None, description='', alias='667')
    CPProgram: Optional[int] = Field(None, description='', alias='875')
    CPRegType: Optional[str] = Field(None, description='', alias='876')
    DatedDate: Optional[date] = Field(None, description='', alias='873')
    InterestAccrualDate: Optional[date] = Field(None, description='', alias='874')
    SecAltIDGrp: Optional[str] = Field(None)
    EvntGrp: Optional[str] = Field(None)
