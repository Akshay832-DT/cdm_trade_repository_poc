"""
FIX 4.4 PreAllocMlegGrp Component

This module contains the Pydantic model for the PreAllocMlegGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoAllocsGroup(FIXComponentBase):
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


class PreAllocMlegGrpComponent(FIXComponentBase):
    """
    FIX 4.4 PreAllocMlegGrp Component
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
    
    NestedParties3: Optional[NestedParties3Component] = Field(None, description='NestedParties3 component')
    NoAllocs: Optional[int] = Field(None, description='Number of NoAllocs entries', alias='')
    NoAllocs_items: List[NoAllocsGroup] = Field(default_factory=list)
