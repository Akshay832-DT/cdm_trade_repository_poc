"""
FIX 4.4 NestedParties Component

This module contains the Pydantic model for the NestedParties component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class NestedParties(FIXMessageBase):
    """
    FIX 4.4 NestedParties Component
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
    nestedPartyID: Optional[str] = Field(None, description='', alias='524')
    nestedPartyIDSource: Optional[str] = Field(None, description='', alias='525')
    nestedPartyRole: Optional[int] = Field(None, description='', alias='538')
    nstdPtysSubGrp: Optional[str] = Field(None)


class NoNestedPartyIDs(FIXMessageBase):
    """
    NoNestedPartyIDs group fields
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
    nestedPartyID: Optional[int] = Field(None, description='', alias='539')
    nestedPartyIDSource: Optional[int] = Field(None, description='', alias='539')
    nestedPartyRole: Optional[int] = Field(None, description='', alias='539')

    noNestedPartyIDss: List[NoNestedPartyIDs] = Field(default_factory=list)
