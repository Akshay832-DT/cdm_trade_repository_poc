"""
FIX 4.4 NestedParties3 Component

This module contains the Pydantic model for the NestedParties3 component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


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
    nested3PartyID: Optional[str] = Field(None, description='', alias='949')
    nested3PartyIDSource: Optional[str] = Field(None, description='', alias='950')
    nested3PartyRole: Optional[int] = Field(None, description='', alias='951')
    nstdPtys3SubGrp: Optional[str] = Field(None)


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
    nested3PartyID: Optional[int] = Field(None, description='', alias='948')
    nested3PartyIDSource: Optional[int] = Field(None, description='', alias='948')
    nested3PartyRole: Optional[int] = Field(None, description='', alias='948')

    noNested3PartyIDss: List[NoNested3PartyIDs] = Field(default_factory=list)
