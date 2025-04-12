"""
FIX 4.4 SideCrossOrdModGrp Component

This module contains the Pydantic model for the SideCrossOrdModGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class SideCrossOrdModGrp(TradeModel):
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
    Side: str = Field(None, description='', alias='54')
    ClOrdID: str = Field(None, description='', alias='11')
    SecondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    ClOrdLinkID: Optional[str] = Field(None, description='', alias='583')
    TradeOriginationDate: Optional[date] = Field(None, description='', alias='229')
    TradeDate: Optional[date] = Field(None, description='', alias='75')
    Account: Optional[str] = Field(None, description='', alias='1')
    AcctIDSource: Optional[int] = Field(None, description='', alias='660')
    AccountType: Optional[int] = Field(None, description='', alias='581')
    DayBookingInst: Optional[str] = Field(None, description='', alias='589')
    BookingUnit: Optional[str] = Field(None, description='', alias='590')
    PreallocMethod: Optional[str] = Field(None, description='', alias='591')
    AllocID: Optional[str] = Field(None, description='', alias='70')
    QtyType: Optional[int] = Field(None, description='', alias='854')
    OrderCapacity: Optional[str] = Field(None, description='', alias='528')
    OrderRestrictions: Optional[List[str]] = Field(None, description='', alias='529')
    CustOrderCapacity: Optional[int] = Field(None, description='', alias='582')
    ForexReq: Optional[bool] = Field(None, description='', alias='121')
    SettlCurrency: Optional[str] = Field(None, description='', alias='120')
    BookingType: Optional[int] = Field(None, description='', alias='775')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    PositionEffect: Optional[str] = Field(None, description='', alias='77')
    CoveredOrUncovered: Optional[int] = Field(None, description='', alias='203')
    CashMargin: Optional[str] = Field(None, description='', alias='544')
    ClearingFeeIndicator: Optional[str] = Field(None, description='', alias='635')
    SolicitedFlag: Optional[bool] = Field(None, description='', alias='377')
    SideComplianceID: Optional[str] = Field(None, description='', alias='659')
    Parties: Optional[str] = Field(None)
    PreAllocGrp: Optional[str] = Field(None)
    OrderQtyData: str = Field(None)
    CommissionData: Optional[str] = Field(None)


class NoSides(TradeModel):
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
    Side: str = Field(None, description='', alias='54')
    ClOrdID: str = Field(None, description='', alias='11')
    SecondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    ClOrdLinkID: Optional[str] = Field(None, description='', alias='583')
    TradeOriginationDate: Optional[date] = Field(None, description='', alias='229')
    TradeDate: Optional[date] = Field(None, description='', alias='75')
    Account: Optional[str] = Field(None, description='', alias='1')
    AcctIDSource: Optional[int] = Field(None, description='', alias='660')
    AccountType: Optional[int] = Field(None, description='', alias='581')
    DayBookingInst: Optional[str] = Field(None, description='', alias='589')
    BookingUnit: Optional[str] = Field(None, description='', alias='590')
    PreallocMethod: Optional[str] = Field(None, description='', alias='591')
    AllocID: Optional[str] = Field(None, description='', alias='70')
    QtyType: Optional[int] = Field(None, description='', alias='854')
    OrderCapacity: Optional[str] = Field(None, description='', alias='528')
    OrderRestrictions: Optional[List[str]] = Field(None, description='', alias='529')
    CustOrderCapacity: Optional[int] = Field(None, description='', alias='582')
    ForexReq: Optional[bool] = Field(None, description='', alias='121')
    SettlCurrency: Optional[str] = Field(None, description='', alias='120')
    BookingType: Optional[int] = Field(None, description='', alias='775')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    PositionEffect: Optional[str] = Field(None, description='', alias='77')
    CoveredOrUncovered: Optional[int] = Field(None, description='', alias='203')
    CashMargin: Optional[str] = Field(None, description='', alias='544')
    ClearingFeeIndicator: Optional[str] = Field(None, description='', alias='635')
    SolicitedFlag: Optional[bool] = Field(None, description='', alias='377')
    SideComplianceID: Optional[str] = Field(None, description='', alias='659')

    NoSidess: List[NoSides] = Field(default_factory=list)
