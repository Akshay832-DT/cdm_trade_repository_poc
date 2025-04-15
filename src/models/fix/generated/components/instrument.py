"""
FIX Component Model - Instrument
"""

from ..base import FIXComponentBase
from .evntgrp import EvntGrpComponent
from .secaltidgrp import SecAltIDGrpComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List




class InstrumentComponent(FIXComponentBase):
    """FIX Component - Instrument"""
    Symbol: Optional[str] = Field(None, alias='55', description='')
    SymbolSfx: Optional[str] = Field(None, alias='65', description='')
    SecurityID: Optional[str] = Field(None, alias='48', description='')
    SecurityIDSource: Optional[str] = Field(None, alias='22', description='')
    Product: Optional[int] = Field(None, alias='460', description='')
    CFICode: Optional[str] = Field(None, alias='461', description='')
    SecurityType: Optional[str] = Field(None, alias='167', description='')
    SecuritySubType: Optional[str] = Field(None, alias='762', description='')
    MaturityMonthYear: Optional[str] = Field(None, alias='200', description='')
    MaturityDate: Optional[date] = Field(None, alias='541', description='')
    PutOrCall: Optional[int] = Field(None, alias='201', description='')
    CouponPaymentDate: Optional[date] = Field(None, alias='224', description='')
    IssueDate: Optional[date] = Field(None, alias='225', description='')
    RepoCollateralSecurityType: Optional[str] = Field(None, alias='239', description='')
    RepurchaseTerm: Optional[int] = Field(None, alias='226', description='')
    RepurchaseRate: Optional[float] = Field(None, alias='227', description='')
    Factor: Optional[float] = Field(None, alias='228', description='')
    CreditRating: Optional[str] = Field(None, alias='255', description='')
    InstrRegistry: Optional[str] = Field(None, alias='543', description='')
    CountryOfIssue: Optional[str] = Field(None, alias='470', description='')
    StateOrProvinceOfIssue: Optional[str] = Field(None, alias='471', description='')
    LocaleOfIssue: Optional[str] = Field(None, alias='472', description='')
    RedemptionDate: Optional[date] = Field(None, alias='240', description='')
    StrikePrice: Optional[float] = Field(None, alias='202', description='')
    StrikeCurrency: Optional[str] = Field(None, alias='947', description='')
    OptAttribute: Optional[str] = Field(None, alias='206', description='')
    ContractMultiplier: Optional[float] = Field(None, alias='231', description='')
    CouponRate: Optional[float] = Field(None, alias='223', description='')
    SecurityExchange: Optional[str] = Field(None, alias='207', description='')
    Issuer: Optional[str] = Field(None, alias='106', description='')
    EncodedIssuerLen: Optional[int] = Field(None, alias='348', description='')
    EncodedIssuer: Optional[str] = Field(None, alias='349', description='')
    SecurityDesc: Optional[str] = Field(None, alias='107', description='')
    EncodedSecurityDescLen: Optional[int] = Field(None, alias='350', description='')
    EncodedSecurityDesc: Optional[str] = Field(None, alias='351', description='')
    Pool: Optional[str] = Field(None, alias='691', description='')
    ContractSettlMonth: Optional[str] = Field(None, alias='667', description='')
    CPProgram: Optional[int] = Field(None, alias='875', description='')
    CPRegType: Optional[str] = Field(None, alias='876', description='')
    DatedDate: Optional[date] = Field(None, alias='873', description='')
    InterestAccrualDate: Optional[date] = Field(None, alias='874', description='')
    SecAltIDGrp: Optional[SecAltIDGrpComponent] = Field(None, description='')
    EvntGrp: Optional[EvntGrpComponent] = Field(None, description='')

