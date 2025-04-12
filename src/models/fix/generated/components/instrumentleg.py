"""
FIX 4.4 InstrumentLeg Component

This module contains the Pydantic model for the InstrumentLeg component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class InstrumentLeg(TradeModel):
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
    LegSymbol: Optional[str] = Field(None, description='', alias='600')
    LegSymbolSfx: Optional[str] = Field(None, description='', alias='601')
    LegSecurityID: Optional[str] = Field(None, description='', alias='602')
    LegSecurityIDSource: Optional[str] = Field(None, description='', alias='603')
    LegProduct: Optional[int] = Field(None, description='', alias='607')
    LegCFICode: Optional[str] = Field(None, description='', alias='608')
    LegSecurityType: Optional[str] = Field(None, description='', alias='609')
    LegSecuritySubType: Optional[str] = Field(None, description='', alias='764')
    LegMaturityMonthYear: Optional[str] = Field(None, description='', alias='610')
    LegMaturityDate: Optional[date] = Field(None, description='', alias='611')
    LegCouponPaymentDate: Optional[date] = Field(None, description='', alias='248')
    LegIssueDate: Optional[date] = Field(None, description='', alias='249')
    LegRepoCollateralSecurityType: Optional[str] = Field(None, description='', alias='250')
    LegRepurchaseTerm: Optional[int] = Field(None, description='', alias='251')
    LegRepurchaseRate: Optional[float] = Field(None, description='', alias='252')
    LegFactor: Optional[float] = Field(None, description='', alias='253')
    LegCreditRating: Optional[str] = Field(None, description='', alias='257')
    LegInstrRegistry: Optional[str] = Field(None, description='', alias='599')
    LegCountryOfIssue: Optional[str] = Field(None, description='', alias='596')
    LegStateOrProvinceOfIssue: Optional[str] = Field(None, description='', alias='597')
    LegLocaleOfIssue: Optional[str] = Field(None, description='', alias='598')
    LegRedemptionDate: Optional[date] = Field(None, description='', alias='254')
    LegStrikePrice: Optional[float] = Field(None, description='', alias='612')
    LegStrikeCurrency: Optional[str] = Field(None, description='', alias='942')
    LegOptAttribute: Optional[str] = Field(None, description='', alias='613')
    LegContractMultiplier: Optional[float] = Field(None, description='', alias='614')
    LegCouponRate: Optional[float] = Field(None, description='', alias='615')
    LegSecurityExchange: Optional[str] = Field(None, description='', alias='616')
    LegIssuer: Optional[str] = Field(None, description='', alias='617')
    EncodedLegIssuerLen: Optional[int] = Field(None, description='', alias='618')
    EncodedLegIssuer: Optional[str] = Field(None, description='', alias='619')
    LegSecurityDesc: Optional[str] = Field(None, description='', alias='620')
    EncodedLegSecurityDescLen: Optional[int] = Field(None, description='', alias='621')
    EncodedLegSecurityDesc: Optional[str] = Field(None, description='', alias='622')
    LegRatioQty: Optional[float] = Field(None, description='', alias='623')
    LegSide: Optional[str] = Field(None, description='', alias='624')
    LegCurrency: Optional[str] = Field(None, description='', alias='556')
    LegPool: Optional[str] = Field(None, description='', alias='740')
    LegDatedDate: Optional[date] = Field(None, description='', alias='739')
    LegContractSettlMonth: Optional[str] = Field(None, description='', alias='955')
    LegInterestAccrualDate: Optional[date] = Field(None, description='', alias='956')
    LegSecAltIDGrp: Optional[str] = Field(None)
