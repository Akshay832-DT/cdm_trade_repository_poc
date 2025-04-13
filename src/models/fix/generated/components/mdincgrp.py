"""
FIX 4.4 MDIncGrp Component

This module contains the Pydantic model for the MDIncGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp


class NoMDEntries(FIXMessageBase):
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
    
    mDUpdateAction: str = Field(..., description='', alias='279')
    deleteReason: Optional[str] = Field(None, description='', alias='285')
    mDEntryType: Optional[str] = Field(None, description='', alias='269')
    mDEntryID: Optional[str] = Field(None, description='', alias='278')
    mDEntryRefID: Optional[str] = Field(None, description='', alias='280')
    financialStatus: Optional[List[str]] = Field(None, description='', alias='291')
    corporateAction: Optional[List[str]] = Field(None, description='', alias='292')
    mDEntryPx: Optional[float] = Field(None, description='', alias='270')
    currency: Optional[str] = Field(None, description='', alias='15')
    mDEntrySize: Optional[float] = Field(None, description='', alias='271')
    mDEntryDate: Optional[date] = Field(None, description='', alias='272')
    mDEntryTime: Optional[time] = Field(None, description='', alias='273')
    tickDirection: Optional[str] = Field(None, description='', alias='274')
    mDMkt: Optional[str] = Field(None, description='', alias='275')
    tradingSessionID: Optional[str] = Field(None, description='', alias='336')
    tradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    quoteCondition: Optional[List[str]] = Field(None, description='', alias='276')
    tradeCondition: Optional[List[str]] = Field(None, description='', alias='277')
    mDEntryOriginator: Optional[str] = Field(None, description='', alias='282')
    locationID: Optional[str] = Field(None, description='', alias='283')
    deskID: Optional[str] = Field(None, description='', alias='284')
    openCloseSettlFlag: Optional[List[str]] = Field(None, description='', alias='286')
    timeInForce: Optional[str] = Field(None, description='', alias='59')
    expireDate: Optional[date] = Field(None, description='', alias='432')
    expireTime: Optional[datetime] = Field(None, description='', alias='126')
    minQty: Optional[float] = Field(None, description='', alias='110')
    execInst: Optional[List[str]] = Field(None, description='', alias='18')
    sellerDays: Optional[int] = Field(None, description='', alias='287')
    orderID: Optional[str] = Field(None, description='', alias='37')
    quoteEntryID: Optional[str] = Field(None, description='', alias='299')
    mDEntryBuyer: Optional[str] = Field(None, description='', alias='288')
    mDEntrySeller: Optional[str] = Field(None, description='', alias='289')
    numberOfOrders: Optional[int] = Field(None, description='', alias='346')
    mDEntryPositionNo: Optional[int] = Field(None, description='', alias='290')
    scope: Optional[List[str]] = Field(None, description='', alias='546')
    priceDelta: Optional[float] = Field(None, description='', alias='811')
    netChgPrevDay: Optional[float] = Field(None, description='', alias='451')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')


class MDIncGrp(FIXMessageBase):
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
    
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    undInstrmtGrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    instrmtLegGrp: Optional[InstrmtLegGrp] = Field(None, description='InstrmtLegGrp component')
    noMDEntries: Optional[int] = Field(None, description='Number of NoMDEntries entries', alias='268')
    noMDEntries_items: List[NoMDEntries] = Field(default_factory=list)
