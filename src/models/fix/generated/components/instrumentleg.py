"""
FIX 4.4 InstrumentLeg Component

This module contains the Pydantic model for the InstrumentLeg component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class InstrumentLeg(FIXMessageBase):
    """
    FIX 4.4 InstrumentLeg Component
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
    legSymbol: Optional[str] = Field(None, description='', alias='600')
    legSymbolSfx: Optional[str] = Field(None, description='', alias='601')
    legSecurityID: Optional[str] = Field(None, description='', alias='602')
    legSecurityIDSource: Optional[str] = Field(None, description='', alias='603')
    legProduct: Optional[int] = Field(None, description='', alias='607')
    legCFICode: Optional[str] = Field(None, description='', alias='608')
    legSecurityType: Optional[str] = Field(None, description='', alias='609')
    legSecuritySubType: Optional[str] = Field(None, description='', alias='764')
    legMaturityMonthYear: Optional[str] = Field(None, description='', alias='610')
    legMaturityDate: Optional[date] = Field(None, description='', alias='611')
    legCouponPaymentDate: Optional[date] = Field(None, description='', alias='248')
    legIssueDate: Optional[date] = Field(None, description='', alias='249')
    legRepoCollateralSecurityType: Optional[str] = Field(None, description='', alias='250')
    legRepurchaseTerm: Optional[int] = Field(None, description='', alias='251')
    legRepurchaseRate: Optional[float] = Field(None, description='', alias='252')
    legFactor: Optional[float] = Field(None, description='', alias='253')
    legCreditRating: Optional[str] = Field(None, description='', alias='257')
    legInstrRegistry: Optional[str] = Field(None, description='', alias='599')
    legCountryOfIssue: Optional[str] = Field(None, description='', alias='596')
    legStateOrProvinceOfIssue: Optional[str] = Field(None, description='', alias='597')
    legLocaleOfIssue: Optional[str] = Field(None, description='', alias='598')
    legRedemptionDate: Optional[date] = Field(None, description='', alias='254')
    legStrikePrice: Optional[float] = Field(None, description='', alias='612')
    legStrikeCurrency: Optional[str] = Field(None, description='', alias='942')
    legOptAttribute: Optional[str] = Field(None, description='', alias='613')
    legContractMultiplier: Optional[float] = Field(None, description='', alias='614')
    legCouponRate: Optional[float] = Field(None, description='', alias='615')
    legSecurityExchange: Optional[str] = Field(None, description='', alias='616')
    legIssuer: Optional[str] = Field(None, description='', alias='617')
    encodedLegIssuerLen: Optional[int] = Field(None, description='', alias='618')
    encodedLegIssuer: Optional[str] = Field(None, description='', alias='619')
    legSecurityDesc: Optional[str] = Field(None, description='', alias='620')
    encodedLegSecurityDescLen: Optional[int] = Field(None, description='', alias='621')
    encodedLegSecurityDesc: Optional[str] = Field(None, description='', alias='622')
    legRatioQty: Optional[float] = Field(None, description='', alias='623')
    legSide: Optional[str] = Field(None, description='', alias='624')
    legCurrency: Optional[str] = Field(None, description='', alias='556')
    legPool: Optional[str] = Field(None, description='', alias='740')
    legDatedDate: Optional[date] = Field(None, description='', alias='739')
    legContractSettlMonth: Optional[str] = Field(None, description='', alias='955')
    legInterestAccrualDate: Optional[date] = Field(None, description='', alias='956')
    legSecAltIDGrp: Optional[str] = Field(None)
