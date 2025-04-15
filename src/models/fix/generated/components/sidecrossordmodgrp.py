"""
FIX Component Model - SideCrossOrdModGrp
"""

from ..base import FIXComponentBase
from .commissiondata import CommissionDataComponent
from .orderqtydata import OrderQtyDataComponent
from .parties import PartiesComponent
from .preallocgrp import PreAllocGrpComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoSidesGroup(FIXComponentBase):

    """FIX Group - NoSides"""

    Side: str = Field(alias='54', description='')
    ClOrdID: str = Field(alias='11', description='')
    SecondaryClOrdID: Optional[str] = Field(None, alias='526', description='')
    ClOrdLinkID: Optional[str] = Field(None, alias='583', description='')
    TradeOriginationDate: Optional[date] = Field(None, alias='229', description='')
    TradeDate: Optional[date] = Field(None, alias='75', description='')
    Account: Optional[str] = Field(None, alias='1', description='')
    AcctIDSource: Optional[int] = Field(None, alias='660', description='')
    AccountType: Optional[int] = Field(None, alias='581', description='')
    DayBookingInst: Optional[str] = Field(None, alias='589', description='')
    BookingUnit: Optional[str] = Field(None, alias='590', description='')
    PreallocMethod: Optional[str] = Field(None, alias='591', description='')
    AllocID: Optional[str] = Field(None, alias='70', description='')
    QtyType: Optional[int] = Field(None, alias='854', description='')
    OrderCapacity: Optional[str] = Field(None, alias='528', description='')
    OrderRestrictions: Optional[str] = Field(None, alias='529', description='')
    CustOrderCapacity: Optional[int] = Field(None, alias='582', description='')
    ForexReq: Optional[bool] = Field(None, alias='121', description='')
    SettlCurrency: Optional[str] = Field(None, alias='120', description='')
    BookingType: Optional[int] = Field(None, alias='775', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    PositionEffect: Optional[str] = Field(None, alias='77', description='')
    CoveredOrUncovered: Optional[int] = Field(None, alias='203', description='')
    CashMargin: Optional[str] = Field(None, alias='544', description='')
    ClearingFeeIndicator: Optional[str] = Field(None, alias='635', description='')
    SolicitedFlag: Optional[bool] = Field(None, alias='377', description='')
    SideComplianceID: Optional[str] = Field(None, alias='659', description='')
    Parties: Optional[PartiesComponent] = Field(None, description='')
    PreAllocGrp: Optional[PreAllocGrpComponent] = Field(None, description='')
    OrderQtyData: OrderQtyDataComponent
    CommissionData: Optional[CommissionDataComponent] = Field(None, description='')



class SideCrossOrdModGrpComponent(FIXComponentBase):
    """FIX Component - SideCrossOrdModGrp"""


