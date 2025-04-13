"""
FIX 4.4 PreAllocGrp Component

This module contains the Pydantic model for the PreAllocGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.nestedparties import NestedParties


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


class PreAllocGrp(FIXMessageBase):
    """
    FIX 4.4 PreAllocGrp Component
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
    
    nestedParties: Optional[NestedParties] = Field(None, description='NestedParties component')
    noAllocs: Optional[int] = Field(None, description='Number of NoAllocs entries', alias='78')
    noAllocs_items: List[NoAllocs] = Field(default_factory=list)
