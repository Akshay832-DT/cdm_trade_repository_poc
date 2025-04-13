"""
FIX 4.4 TrdAllocGrp Component

This module contains the Pydantic model for the TrdAllocGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.nestedparties2 import NestedParties2


class NoAllocs(FIXMessageBase):
    """
    NoAllocs group fields
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
    
    allocAccount: Optional[str] = Field(None, description='', alias='79')
    allocAcctIDSource: Optional[int] = Field(None, description='', alias='661')
    allocSettlCurrency: Optional[str] = Field(None, description='', alias='736')
    individualAllocID: Optional[str] = Field(None, description='', alias='467')
    allocQty: Optional[float] = Field(None, description='', alias='80')


class TrdAllocGrp(FIXMessageBase):
    """
    FIX 4.4 TrdAllocGrp Component
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
    noAllocs: Optional[int] = Field(None, description='Number of NoAllocs entries', alias='78')
    noAllocs_items: List[NoAllocs] = Field(default_factory=list)
