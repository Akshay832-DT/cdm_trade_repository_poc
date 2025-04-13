"""
FIX 4.4 LegPreAllocGrp Component

This module contains the Pydantic model for the LegPreAllocGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoLegAllocsGroup(FIXComponentBase):
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


class LegPreAllocGrpComponent(FIXComponentBase):
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
    
    NestedParties2: Optional[NestedParties2Component] = Field(None, description='NestedParties2 component')
    NoLegAllocs: Optional[int] = Field(None, description='Number of NoLegAllocs entries', alias='')
    NoLegAllocs_items: List[NoLegAllocsGroup] = Field(default_factory=list)
