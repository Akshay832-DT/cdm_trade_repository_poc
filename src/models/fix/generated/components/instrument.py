"""
FIX 4.4 Instrument Component

This module contains the Pydantic model for the Instrument component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.secaltidgrp import SecAltIDGrp
from src.models.fix.generated.components.evntgrp import EvntGrp


class Instrument(FIXMessageBase):
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
    
    symbol: Optional[str] = Field(None, description='', alias='55')
    symbolSfx: Optional[str] = Field(None, description='', alias='65')
    securityID: Optional[str] = Field(None, description='', alias='48')
    securityIDSource: Optional[str] = Field(None, description='', alias='22')
    product: Optional[int] = Field(None, description='', alias='460')
    cFICode: Optional[str] = Field(None, description='', alias='461')
    securityType: Optional[str] = Field(None, description='', alias='167')
    securitySubType: Optional[str] = Field(None, description='', alias='762')
    maturityMonthYear: Optional[str] = Field(None, description='', alias='200')
    maturityDate: Optional[date] = Field(None, description='', alias='541')
    putOrCall: Optional[int] = Field(None, description='', alias='201')
    couponPaymentDate: Optional[date] = Field(None, description='', alias='224')
    issueDate: Optional[date] = Field(None, description='', alias='225')
    repoCollateralSecurityType: Optional[str] = Field(None, description='', alias='239')
    repurchaseTerm: Optional[int] = Field(None, description='', alias='226')
    repurchaseRate: Optional[float] = Field(None, description='', alias='227')
    factor: Optional[float] = Field(None, description='', alias='228')
    creditRating: Optional[str] = Field(None, description='', alias='255')
    instrRegistry: Optional[str] = Field(None, description='', alias='543')
    countryOfIssue: Optional[str] = Field(None, description='', alias='470')
    stateOrProvinceOfIssue: Optional[str] = Field(None, description='', alias='471')
    localeOfIssue: Optional[str] = Field(None, description='', alias='472')
    redemptionDate: Optional[date] = Field(None, description='', alias='240')
    strikePrice: Optional[float] = Field(None, description='', alias='202')
    strikeCurrency: Optional[str] = Field(None, description='', alias='947')
    optAttribute: Optional[str] = Field(None, description='', alias='206')
    contractMultiplier: Optional[float] = Field(None, description='', alias='231')
    couponRate: Optional[float] = Field(None, description='', alias='223')
    securityExchange: Optional[str] = Field(None, description='', alias='207')
    issuer: Optional[str] = Field(None, description='', alias='106')
    encodedIssuerLen: Optional[int] = Field(None, description='', alias='348')
    encodedIssuer: Optional[str] = Field(None, description='', alias='349')
    securityDesc: Optional[str] = Field(None, description='', alias='107')
    encodedSecurityDescLen: Optional[int] = Field(None, description='', alias='350')
    encodedSecurityDesc: Optional[str] = Field(None, description='', alias='351')
    pool: Optional[str] = Field(None, description='', alias='691')
    contractSettlMonth: Optional[str] = Field(None, description='', alias='667')
    cPProgram: Optional[int] = Field(None, description='', alias='875')
    cPRegType: Optional[str] = Field(None, description='', alias='876')
    datedDate: Optional[date] = Field(None, description='', alias='873')
    interestAccrualDate: Optional[date] = Field(None, description='', alias='874')
    secAltIDGrp: Optional[SecAltIDGrp] = Field(None, description='SecAltIDGrp component')
    evntGrp: Optional[EvntGrp] = Field(None, description='EvntGrp component')
