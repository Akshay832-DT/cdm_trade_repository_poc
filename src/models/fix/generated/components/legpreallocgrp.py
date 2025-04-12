"""
FIX 4.4 LegPreAllocGrp Component

This module contains the Pydantic model for the LegPreAllocGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class LegPreAllocGrp(TradeModel):
    """
    FIX 4.4 LegPreAllocGrp Component
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
    LegAllocAccount: Optional[str] = Field(None, description='', alias='671')
    LegIndividualAllocID: Optional[str] = Field(None, description='', alias='672')
    LegAllocQty: Optional[float] = Field(None, description='', alias='673')
    LegAllocAcctIDSource: Optional[str] = Field(None, description='', alias='674')
    LegSettlCurrency: Optional[str] = Field(None, description='', alias='675')
    NestedParties2: Optional[str] = Field(None)


class NoLegAllocs(TradeModel):
    """
    NoLegAllocs group fields
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
    LegAllocAccount: Optional[str] = Field(None, description='', alias='671')
    LegIndividualAllocID: Optional[str] = Field(None, description='', alias='672')
    LegAllocQty: Optional[float] = Field(None, description='', alias='673')
    LegAllocAcctIDSource: Optional[str] = Field(None, description='', alias='674')
    LegSettlCurrency: Optional[str] = Field(None, description='', alias='675')

    NoLegAllocss: List[NoLegAllocs] = Field(default_factory=list)
