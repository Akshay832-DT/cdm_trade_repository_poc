"""
FIX 4.4 NestedParties Component

This module contains the Pydantic model for the NestedParties component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.nstdptyssubgrp import NstdPtysSubGrp


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
    
    nestedPartyID: Optional[str] = Field(None, description='', alias='524')
    nestedPartyIDSource: Optional[str] = Field(None, description='', alias='525')
    nestedPartyRole: Optional[int] = Field(None, description='', alias='538')
    nstdPtysSubGrp: Optional[NstdPtysSubGrp] = Field(None, description='NstdPtysSubGrp component')


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
    
    noNestedPartyIDs: Optional[int] = Field(None, description='Number of NoNestedPartyIDs entries', alias='539')
    noNestedPartyIDs_items: List[NoNestedPartyIDs] = Field(default_factory=list)
