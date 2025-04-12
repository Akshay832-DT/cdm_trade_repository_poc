"""
FIX 4.4 SettlPtysSubGrp Component

This module contains the Pydantic model for the SettlPtysSubGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class SettlPtysSubGrp(FIXMessageBase):
    """
    FIX 4.4 SettlPtysSubGrp Component
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
    settlPartySubID: Optional[str] = Field(None, description='', alias='785')
    settlPartySubIDType: Optional[int] = Field(None, description='', alias='786')


class NoSettlPartySubIDs(FIXMessageBase):
    """
    NoSettlPartySubIDs group fields
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
    settlPartySubID: Optional[int] = Field(None, description='', alias='801')
    settlPartySubIDType: Optional[int] = Field(None, description='', alias='801')

    noSettlPartySubIDss: List[NoSettlPartySubIDs] = Field(default_factory=list)
