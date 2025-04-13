"""
FIX 4.4 RoutingGrp Component

This module contains the Pydantic model for the RoutingGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoRoutingIDsGroup(FIXComponentBase):
    """
    NoRoutingIDs group fields
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
    
    RoutingType: Optional[int] = Field(None, description='', alias='216')
    RoutingID: Optional[str] = Field(None, description='', alias='217')


class RoutingGrpComponent(FIXComponentBase):
    """
    FIX 4.4 RoutingGrp Component
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
    
    NoRoutingIDs: Optional[int] = Field(None, description='Number of NoRoutingIDs entries', alias='')
    NoRoutingIDs_items: List[NoRoutingIDsGroup] = Field(default_factory=list)
