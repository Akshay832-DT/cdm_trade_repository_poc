"""
FIX 4.4 NestedParties2 Component

This module contains the Pydantic model for the NestedParties2 component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.nstdptys2subgrp import NstdPtys2SubGrp


class NoNested2PartyIDs(FIXMessageBase):
    """
    NoNested2PartyIDs group fields
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
    
    nested2PartyID: Optional[str] = Field(None, description='', alias='757')
    nested2PartyIDSource: Optional[str] = Field(None, description='', alias='758')
    nested2PartyRole: Optional[int] = Field(None, description='', alias='759')
    nstdPtys2SubGrp: Optional[NstdPtys2SubGrp] = Field(None, description='NstdPtys2SubGrp component')


class NestedParties2(FIXMessageBase):
    """
    FIX 4.4 NestedParties2 Component
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
    
    noNested2PartyIDs: Optional[int] = Field(None, description='Number of NoNested2PartyIDs entries', alias='756')
    noNested2PartyIDs_items: List[NoNested2PartyIDs] = Field(default_factory=list)
