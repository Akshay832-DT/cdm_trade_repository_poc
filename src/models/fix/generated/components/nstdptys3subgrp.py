"""
FIX 4.4 NstdPtys3SubGrp Component

This module contains the Pydantic model for the NstdPtys3SubGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class NstdPtys3SubGrp(FIXMessageBase):
    """
    FIX 4.4 NstdPtys3SubGrp Component
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
    nested3PartySubID: Optional[str] = Field(None, description='', alias='953')
    nested3PartySubIDType: Optional[int] = Field(None, description='', alias='954')


class NoNested3PartySubIDs(FIXMessageBase):
    """
    NoNested3PartySubIDs group fields
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
    nested3PartySubID: Optional[int] = Field(None, description='', alias='952')
    nested3PartySubIDType: Optional[int] = Field(None, description='', alias='952')

    noNested3PartySubIDss: List[NoNested3PartySubIDs] = Field(default_factory=list)
