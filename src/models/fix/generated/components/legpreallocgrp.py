"""
FIX 4.4 LegPreAllocGrp Component

This module contains the Pydantic model for the LegPreAllocGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class LegPreAllocGrp(FIXMessageBase):
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
    legAllocAccount: Optional[str] = Field(None, description='', alias='671')
    legIndividualAllocID: Optional[str] = Field(None, description='', alias='672')
    legAllocQty: Optional[float] = Field(None, description='', alias='673')
    legAllocAcctIDSource: Optional[str] = Field(None, description='', alias='674')
    legSettlCurrency: Optional[str] = Field(None, description='', alias='675')
    nestedParties2: Optional[str] = Field(None)


class NoLegAllocs(FIXMessageBase):
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
    legAllocAccount: Optional[int] = Field(None, description='', alias='670')
    legIndividualAllocID: Optional[int] = Field(None, description='', alias='670')
    legAllocQty: Optional[int] = Field(None, description='', alias='670')
    legAllocAcctIDSource: Optional[int] = Field(None, description='', alias='670')
    legSettlCurrency: Optional[int] = Field(None, description='', alias='670')

    noLegAllocss: List[NoLegAllocs] = Field(default_factory=list)
