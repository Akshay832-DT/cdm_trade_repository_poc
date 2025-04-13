"""
FIX 4.4 OrdAllocGrp Component

This module contains the Pydantic model for the OrdAllocGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.nestedparties2 import NestedParties2


class NoOrders(FIXMessageBase):
    """
    NoOrders group fields
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
    
    clOrdID: Optional[str] = Field(None, description='', alias='11')
    orderID: Optional[str] = Field(None, description='', alias='37')
    secondaryOrderID: Optional[str] = Field(None, description='', alias='198')
    secondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    listID: Optional[str] = Field(None, description='', alias='66')
    orderQty: Optional[float] = Field(None, description='', alias='38')
    orderAvgPx: Optional[float] = Field(None, description='', alias='799')
    orderBookingQty: Optional[float] = Field(None, description='', alias='800')


class OrdAllocGrp(FIXMessageBase):
    """
    FIX 4.4 OrdAllocGrp Component
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
    
    nestedParties2: Optional[NestedParties2] = Field(None, description='NestedParties2 component')
    noOrders: Optional[int] = Field(None, description='Number of NoOrders entries', alias='73')
    noOrders_items: List[NoOrders] = Field(default_factory=list)
