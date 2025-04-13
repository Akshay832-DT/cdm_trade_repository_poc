"""
FIX 4.4 OrdAllocGrp Component

This module contains the Pydantic model for the OrdAllocGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoOrdersGroup(FIXComponentBase):
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
    
    ClOrdID: Optional[str] = Field(None, description='', alias='11')
    OrderID: Optional[str] = Field(None, description='', alias='37')
    SecondaryOrderID: Optional[str] = Field(None, description='', alias='198')
    SecondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    ListID: Optional[str] = Field(None, description='', alias='66')
    OrderQty: Optional[float] = Field(None, description='', alias='38')
    OrderAvgPx: Optional[float] = Field(None, description='', alias='799')
    OrderBookingQty: Optional[float] = Field(None, description='', alias='800')


class OrdAllocGrpComponent(FIXComponentBase):
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
    
    NestedParties2: Optional[NestedParties2Component] = Field(None, description='NestedParties2 component')
    NoOrders: Optional[int] = Field(None, description='Number of NoOrders entries', alias='')
    NoOrders_items: List[NoOrdersGroup] = Field(default_factory=list)
