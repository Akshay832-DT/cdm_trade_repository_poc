"""
FIX 4.4 PreAllocGrp Component

This module contains the Pydantic model for the PreAllocGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class PreAllocGrp(TradeModel):
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
    AllocAccount: Optional[str] = Field(None, description='', alias='79')
    AllocAcctIDSource: Optional[int] = Field(None, description='', alias='661')
    AllocSettlCurrency: Optional[str] = Field(None, description='', alias='736')
    IndividualAllocID: Optional[str] = Field(None, description='', alias='467')
    AllocQty: Optional[float] = Field(None, description='', alias='80')
    NestedParties: Optional[str] = Field(None)


class NoAllocs(TradeModel):
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
    AllocAccount: Optional[str] = Field(None, description='', alias='79')
    AllocAcctIDSource: Optional[int] = Field(None, description='', alias='661')
    AllocSettlCurrency: Optional[str] = Field(None, description='', alias='736')
    IndividualAllocID: Optional[str] = Field(None, description='', alias='467')
    AllocQty: Optional[float] = Field(None, description='', alias='80')

    NoAllocss: List[NoAllocs] = Field(default_factory=list)
