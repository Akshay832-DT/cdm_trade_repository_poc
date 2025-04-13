"""
FIX 4.4 NestedParties3 Component

This module contains the Pydantic model for the NestedParties3 component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.nstdptys3subgrp import NstdPtys3SubGrp


class NoNested3PartyIDs(FIXMessageBase):
    """
    NoNested3PartyIDs group fields
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
    
    nested3PartyID: Optional[str] = Field(None, description='', alias='949')
    nested3PartyIDSource: Optional[str] = Field(None, description='', alias='950')
    nested3PartyRole: Optional[int] = Field(None, description='', alias='951')
    nstdPtys3SubGrp: Optional[NstdPtys3SubGrp] = Field(None, description='NstdPtys3SubGrp component')


class NestedParties3(FIXMessageBase):
    """
    FIX 4.4 NestedParties3 Component
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
    
    noNested3PartyIDs: Optional[int] = Field(None, description='Number of NoNested3PartyIDs entries', alias='948')
    noNested3PartyIDs_items: List[NoNested3PartyIDs] = Field(default_factory=list)
