"""
FIX Component Model - UnderlyingInstrument
"""

from ..base import FIXComponentBase
from .underlyingstipulations import UnderlyingStipulationsComponent
from .undsecaltidgrp import UndSecAltIDGrpComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List




class UnderlyingInstrumentComponent(FIXComponentBase):
    """FIX Component - UnderlyingInstrument"""
    UnderlyingSymbol: Optional[str] = Field(None, alias='311', description='')
    UnderlyingSymbolSfx: Optional[str] = Field(None, alias='312', description='')
    UnderlyingSecurityID: Optional[str] = Field(None, alias='309', description='')
    UnderlyingSecurityIDSource: Optional[str] = Field(None, alias='305', description='')
    UnderlyingProduct: Optional[int] = Field(None, alias='462', description='')
    UnderlyingCFICode: Optional[str] = Field(None, alias='463', description='')
    UnderlyingSecurityType: Optional[str] = Field(None, alias='310', description='')
    UnderlyingSecuritySubType: Optional[str] = Field(None, alias='763', description='')
    UnderlyingMaturityMonthYear: Optional[str] = Field(None, alias='313', description='')
    UnderlyingMaturityDate: Optional[date] = Field(None, alias='542', description='')
    UnderlyingPutOrCall: Optional[int] = Field(None, alias='315', description='')
    UnderlyingCouponPaymentDate: Optional[date] = Field(None, alias='241', description='')
    UnderlyingIssueDate: Optional[date] = Field(None, alias='242', description='')
    UnderlyingRepoCollateralSecurityType: Optional[str] = Field(None, alias='243', description='')
    UnderlyingRepurchaseTerm: Optional[int] = Field(None, alias='244', description='')
    UnderlyingRepurchaseRate: Optional[float] = Field(None, alias='245', description='')
    UnderlyingFactor: Optional[float] = Field(None, alias='246', description='')
    UnderlyingCreditRating: Optional[str] = Field(None, alias='256', description='')
    UnderlyingInstrRegistry: Optional[str] = Field(None, alias='595', description='')
    UnderlyingCountryOfIssue: Optional[str] = Field(None, alias='592', description='')
    UnderlyingStateOrProvinceOfIssue: Optional[str] = Field(None, alias='593', description='')
    UnderlyingLocaleOfIssue: Optional[str] = Field(None, alias='594', description='')
    UnderlyingRedemptionDate: Optional[date] = Field(None, alias='247', description='')
    UnderlyingStrikePrice: Optional[float] = Field(None, alias='316', description='')
    UnderlyingStrikeCurrency: Optional[str] = Field(None, alias='941', description='')
    UnderlyingOptAttribute: Optional[str] = Field(None, alias='317', description='')
    UnderlyingContractMultiplier: Optional[float] = Field(None, alias='436', description='')
    UnderlyingCouponRate: Optional[float] = Field(None, alias='435', description='')
    UnderlyingSecurityExchange: Optional[str] = Field(None, alias='308', description='')
    UnderlyingIssuer: Optional[str] = Field(None, alias='306', description='')
    EncodedUnderlyingIssuerLen: Optional[int] = Field(None, alias='362', description='')
    EncodedUnderlyingIssuer: Optional[str] = Field(None, alias='363', description='')
    UnderlyingSecurityDesc: Optional[str] = Field(None, alias='307', description='')
    EncodedUnderlyingSecurityDescLen: Optional[int] = Field(None, alias='364', description='')
    EncodedUnderlyingSecurityDesc: Optional[str] = Field(None, alias='365', description='')
    UnderlyingCPProgram: Optional[str] = Field(None, alias='877', description='')
    UnderlyingCPRegType: Optional[str] = Field(None, alias='878', description='')
    UnderlyingCurrency: Optional[str] = Field(None, alias='318', description='')
    UnderlyingQty: Optional[float] = Field(None, alias='879', description='')
    UnderlyingPx: Optional[float] = Field(None, alias='810', description='')
    UnderlyingDirtyPrice: Optional[float] = Field(None, alias='882', description='')
    UnderlyingEndPrice: Optional[float] = Field(None, alias='883', description='')
    UnderlyingStartValue: Optional[float] = Field(None, alias='884', description='')
    UnderlyingCurrentValue: Optional[float] = Field(None, alias='885', description='')
    UnderlyingEndValue: Optional[float] = Field(None, alias='886', description='')
    UndSecAltIDGrp: Optional[UndSecAltIDGrpComponent] = Field(None, description='')
    UnderlyingStipulations: Optional[UnderlyingStipulationsComponent] = Field(None, description='')

