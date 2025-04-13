"""
FIX 4.4 SideCrossOrdCxlGrp Component

This module contains the Pydantic model for the SideCrossOrdCxlGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.parties import Parties
from src.models.fix.generated.components.orderqtydata import OrderQtyData


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
    
    side: str = Field(..., description='', alias='54')
    origClOrdID: str = Field(..., description='', alias='41')
    clOrdID: str = Field(..., description='', alias='11')
    secondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    clOrdLinkID: Optional[str] = Field(None, description='', alias='583')
    origOrdModTime: Optional[datetime] = Field(None, description='', alias='586')
    tradeOriginationDate: Optional[date] = Field(None, description='', alias='229')
    tradeDate: Optional[date] = Field(None, description='', alias='75')
    complianceID: Optional[str] = Field(None, description='', alias='376')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')


class SideCrossOrdCxlGrp(FIXMessageBase):
    """
    FIX 4.4 SideCrossOrdCxlGrp Component
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
    
    parties: Optional[Parties] = Field(None, description='Parties component')
    orderQtyData: OrderQtyData = Field(..., description='OrderQtyData component')
    noSides: Optional[int] = Field(None, description='Number of NoSides entries', alias='552')
    noSides_items: List[NoSides] = Field(default_factory=list)
