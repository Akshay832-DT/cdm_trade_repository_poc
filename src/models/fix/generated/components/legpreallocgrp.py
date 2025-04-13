"""
FIX 4.4 LegPreAllocGrp Component

This module contains the Pydantic model for the LegPreAllocGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.nestedparties2 import NestedParties2


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
    
    legAllocAccount: Optional[str] = Field(None, description='', alias='671')
    legIndividualAllocID: Optional[str] = Field(None, description='', alias='672')
    legAllocQty: Optional[float] = Field(None, description='', alias='673')
    legAllocAcctIDSource: Optional[str] = Field(None, description='', alias='674')
    legSettlCurrency: Optional[str] = Field(None, description='', alias='675')


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
    
    nestedParties2: Optional[NestedParties2] = Field(None, description='NestedParties2 component')
    noLegAllocs: Optional[int] = Field(None, description='Number of NoLegAllocs entries', alias='670')
    noLegAllocs_items: List[NoLegAllocs] = Field(default_factory=list)
