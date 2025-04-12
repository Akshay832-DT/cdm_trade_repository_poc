"""
FIX 4.4 SideCrossOrdModGrp Component

This module contains the Pydantic model for the SideCrossOrdModGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class SideCrossOrdModGrp(FIXMessageBase):
    """
    FIX 4.4 SideCrossOrdModGrp Component
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
    side: str = Field(None, description='', alias='54')
    clOrdID: str = Field(None, description='', alias='11')
    secondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    clOrdLinkID: Optional[str] = Field(None, description='', alias='583')
    tradeOriginationDate: Optional[date] = Field(None, description='', alias='229')
    tradeDate: Optional[date] = Field(None, description='', alias='75')
    account: Optional[str] = Field(None, description='', alias='1')
    acctIDSource: Optional[int] = Field(None, description='', alias='660')
    accountType: Optional[int] = Field(None, description='', alias='581')
    dayBookingInst: Optional[str] = Field(None, description='', alias='589')
    bookingUnit: Optional[str] = Field(None, description='', alias='590')
    preallocMethod: Optional[str] = Field(None, description='', alias='591')
    allocID: Optional[str] = Field(None, description='', alias='70')
    qtyType: Optional[int] = Field(None, description='', alias='854')
    orderCapacity: Optional[str] = Field(None, description='', alias='528')
    orderRestrictions: Optional[List[str]] = Field(None, description='', alias='529')
    custOrderCapacity: Optional[int] = Field(None, description='', alias='582')
    forexReq: Optional[bool] = Field(None, description='', alias='121')
    settlCurrency: Optional[str] = Field(None, description='', alias='120')
    bookingType: Optional[int] = Field(None, description='', alias='775')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')
    positionEffect: Optional[str] = Field(None, description='', alias='77')
    coveredOrUncovered: Optional[int] = Field(None, description='', alias='203')
    cashMargin: Optional[str] = Field(None, description='', alias='544')
    clearingFeeIndicator: Optional[str] = Field(None, description='', alias='635')
    solicitedFlag: Optional[bool] = Field(None, description='', alias='377')
    sideComplianceID: Optional[str] = Field(None, description='', alias='659')
    parties: Optional[str] = Field(None)
    preAllocGrp: Optional[str] = Field(None)
    orderQtyData: str = Field(None)
    commissionData: Optional[str] = Field(None)


class NoSides(FIXMessageBase):
    """
    NoSides group fields
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
    side: int = Field(None, description='', alias='552')
    clOrdID: int = Field(None, description='', alias='552')
    secondaryClOrdID: Optional[int] = Field(None, description='', alias='552')
    clOrdLinkID: Optional[int] = Field(None, description='', alias='552')
    tradeOriginationDate: Optional[int] = Field(None, description='', alias='552')
    tradeDate: Optional[int] = Field(None, description='', alias='552')
    account: Optional[int] = Field(None, description='', alias='552')
    acctIDSource: Optional[int] = Field(None, description='', alias='552')
    accountType: Optional[int] = Field(None, description='', alias='552')
    dayBookingInst: Optional[int] = Field(None, description='', alias='552')
    bookingUnit: Optional[int] = Field(None, description='', alias='552')
    preallocMethod: Optional[int] = Field(None, description='', alias='552')
    allocID: Optional[int] = Field(None, description='', alias='552')
    qtyType: Optional[int] = Field(None, description='', alias='552')
    orderCapacity: Optional[int] = Field(None, description='', alias='552')
    orderRestrictions: Optional[int] = Field(None, description='', alias='552')
    custOrderCapacity: Optional[int] = Field(None, description='', alias='552')
    forexReq: Optional[int] = Field(None, description='', alias='552')
    settlCurrency: Optional[int] = Field(None, description='', alias='552')
    bookingType: Optional[int] = Field(None, description='', alias='552')
    text: Optional[int] = Field(None, description='', alias='552')
    encodedTextLen: Optional[int] = Field(None, description='', alias='552')
    encodedText: Optional[int] = Field(None, description='', alias='552')
    positionEffect: Optional[int] = Field(None, description='', alias='552')
    coveredOrUncovered: Optional[int] = Field(None, description='', alias='552')
    cashMargin: Optional[int] = Field(None, description='', alias='552')
    clearingFeeIndicator: Optional[int] = Field(None, description='', alias='552')
    solicitedFlag: Optional[int] = Field(None, description='', alias='552')
    sideComplianceID: Optional[int] = Field(None, description='', alias='552')

    noSidess: List[NoSides] = Field(default_factory=list)
