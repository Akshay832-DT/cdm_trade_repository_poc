"""
FIX Component Model - InstrumentLeg
"""

from ..base import FIXComponentBase
from .legsecaltidgrp import LegSecAltIDGrpComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List




class InstrumentLegComponent(FIXComponentBase):
    """FIX Component - InstrumentLeg"""
    LegSymbol: Optional[str] = Field(None, alias='600', description='')
    LegSymbolSfx: Optional[str] = Field(None, alias='601', description='')
    LegSecurityID: Optional[str] = Field(None, alias='602', description='')
    LegSecurityIDSource: Optional[str] = Field(None, alias='603', description='')
    LegProduct: Optional[int] = Field(None, alias='607', description='')
    LegCFICode: Optional[str] = Field(None, alias='608', description='')
    LegSecurityType: Optional[str] = Field(None, alias='609', description='')
    LegSecuritySubType: Optional[str] = Field(None, alias='764', description='')
    LegMaturityMonthYear: Optional[str] = Field(None, alias='610', description='')
    LegMaturityDate: Optional[date] = Field(None, alias='611', description='')
    LegCouponPaymentDate: Optional[date] = Field(None, alias='248', description='')
    LegIssueDate: Optional[date] = Field(None, alias='249', description='')
    LegRepoCollateralSecurityType: Optional[str] = Field(None, alias='250', description='')
    LegRepurchaseTerm: Optional[int] = Field(None, alias='251', description='')
    LegRepurchaseRate: Optional[float] = Field(None, alias='252', description='')
    LegFactor: Optional[float] = Field(None, alias='253', description='')
    LegCreditRating: Optional[str] = Field(None, alias='257', description='')
    LegInstrRegistry: Optional[str] = Field(None, alias='599', description='')
    LegCountryOfIssue: Optional[str] = Field(None, alias='596', description='')
    LegStateOrProvinceOfIssue: Optional[str] = Field(None, alias='597', description='')
    LegLocaleOfIssue: Optional[str] = Field(None, alias='598', description='')
    LegRedemptionDate: Optional[date] = Field(None, alias='254', description='')
    LegStrikePrice: Optional[float] = Field(None, alias='612', description='')
    LegStrikeCurrency: Optional[str] = Field(None, alias='942', description='')
    LegOptAttribute: Optional[str] = Field(None, alias='613', description='')
    LegContractMultiplier: Optional[float] = Field(None, alias='614', description='')
    LegCouponRate: Optional[float] = Field(None, alias='615', description='')
    LegSecurityExchange: Optional[str] = Field(None, alias='616', description='')
    LegIssuer: Optional[str] = Field(None, alias='617', description='')
    EncodedLegIssuerLen: Optional[int] = Field(None, alias='618', description='')
    EncodedLegIssuer: Optional[str] = Field(None, alias='619', description='')
    LegSecurityDesc: Optional[str] = Field(None, alias='620', description='')
    EncodedLegSecurityDescLen: Optional[int] = Field(None, alias='621', description='')
    EncodedLegSecurityDesc: Optional[str] = Field(None, alias='622', description='')
    LegRatioQty: Optional[float] = Field(None, alias='623', description='')
    LegSide: Optional[str] = Field(None, alias='624', description='')
    LegCurrency: Optional[str] = Field(None, alias='556', description='')
    LegPool: Optional[str] = Field(None, alias='740', description='')
    LegDatedDate: Optional[date] = Field(None, alias='739', description='')
    LegContractSettlMonth: Optional[str] = Field(None, alias='955', description='')
    LegInterestAccrualDate: Optional[date] = Field(None, alias='956', description='')
    LegSecAltIDGrp: Optional[LegSecAltIDGrpComponent] = Field(None, description='')

