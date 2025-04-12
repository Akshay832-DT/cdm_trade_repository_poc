"""
FIX 4.4 CompIDReqGrp Component

This module contains the Pydantic model for the CompIDReqGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class CompIDReqGrp(TradeModel):
    """
    FIX 4.4 CompIDReqGrp Component
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
    RefCompID: Optional[str] = Field(None, description='', alias='930')
    RefSubID: Optional[str] = Field(None, description='', alias='931')
    LocationID: Optional[str] = Field(None, description='', alias='283')
    DeskID: Optional[str] = Field(None, description='', alias='284')


class NoCompIDs(TradeModel):
    """
    NoCompIDs group fields
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
    RefCompID: Optional[str] = Field(None, description='', alias='930')
    RefSubID: Optional[str] = Field(None, description='', alias='931')
    LocationID: Optional[str] = Field(None, description='', alias='283')
    DeskID: Optional[str] = Field(None, description='', alias='284')

    NoCompIDss: List[NoCompIDs] = Field(default_factory=list)
