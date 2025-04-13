"""
FIX 4.4 MDIncGrp Component

This module contains the Pydantic model for the MDIncGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoMDEntriesGroup(FIXComponentBase):
    """
    NoMDEntries group fields
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
    
    MDUpdateAction: str = Field(..., description='', alias='279')
    DeleteReason: Optional[str] = Field(None, description='', alias='285')
    MDEntryType: Optional[str] = Field(None, description='', alias='269')
    MDEntryID: Optional[str] = Field(None, description='', alias='278')
    MDEntryRefID: Optional[str] = Field(None, description='', alias='280')
    FinancialStatus: Optional[List[str]] = Field(None, description='', alias='291')
    CorporateAction: Optional[List[str]] = Field(None, description='', alias='292')
    MDEntryPx: Optional[float] = Field(None, description='', alias='270')
    Currency: Optional[str] = Field(None, description='', alias='15')
    MDEntrySize: Optional[float] = Field(None, description='', alias='271')
    MDEntryDate: Optional[date] = Field(None, description='', alias='272')
    MDEntryTime: Optional[time] = Field(None, description='', alias='273')
    TickDirection: Optional[str] = Field(None, description='', alias='274')
    MDMkt: Optional[str] = Field(None, description='', alias='275')
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    QuoteCondition: Optional[List[str]] = Field(None, description='', alias='276')
    TradeCondition: Optional[List[str]] = Field(None, description='', alias='277')
    MDEntryOriginator: Optional[str] = Field(None, description='', alias='282')
    LocationID: Optional[str] = Field(None, description='', alias='283')
    DeskID: Optional[str] = Field(None, description='', alias='284')
    OpenCloseSettlFlag: Optional[List[str]] = Field(None, description='', alias='286')
    TimeInForce: Optional[str] = Field(None, description='', alias='59')
    ExpireDate: Optional[date] = Field(None, description='', alias='432')
    ExpireTime: Optional[datetime] = Field(None, description='', alias='126')
    MinQty: Optional[float] = Field(None, description='', alias='110')
    ExecInst: Optional[List[str]] = Field(None, description='', alias='18')
    SellerDays: Optional[int] = Field(None, description='', alias='287')
    OrderID: Optional[str] = Field(None, description='', alias='37')
    QuoteEntryID: Optional[str] = Field(None, description='', alias='299')
    MDEntryBuyer: Optional[str] = Field(None, description='', alias='288')
    MDEntrySeller: Optional[str] = Field(None, description='', alias='289')
    NumberOfOrders: Optional[int] = Field(None, description='', alias='346')
    MDEntryPositionNo: Optional[int] = Field(None, description='', alias='290')
    Scope: Optional[List[str]] = Field(None, description='', alias='546')
    PriceDelta: Optional[float] = Field(None, description='', alias='811')
    NetChgPrevDay: Optional[float] = Field(None, description='', alias='451')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')


class MDIncGrpComponent(FIXComponentBase):
    """
    FIX 4.4 MDIncGrp Component
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
    
    Instrument: Optional[InstrumentComponent] = Field(None, description='Instrument component')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='UndInstrmtGrp component')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='InstrmtLegGrp component')
    NoMDEntries: Optional[int] = Field(None, description='Number of NoMDEntries entries', alias='')
    NoMDEntries_items: List[NoMDEntriesGroup] = Field(default_factory=list)
