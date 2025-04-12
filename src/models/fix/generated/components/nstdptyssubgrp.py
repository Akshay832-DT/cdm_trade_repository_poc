"""
FIX 4.4 NstdPtysSubGrp Component

This module contains the Pydantic model for the NstdPtysSubGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class NstdPtysSubGrp(FIXMessageBase):
    """
    FIX 4.4 NstdPtysSubGrp Component
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
    nestedPartySubID: Optional[str] = Field(None, description='', alias='545')
    nestedPartySubIDType: Optional[int] = Field(None, description='', alias='805')


class NoNestedPartySubIDs(FIXMessageBase):
    """
    NoNestedPartySubIDs group fields
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
    nestedPartySubID: Optional[int] = Field(None, description='', alias='804')
    nestedPartySubIDType: Optional[int] = Field(None, description='', alias='804')

    noNestedPartySubIDss: List[NoNestedPartySubIDs] = Field(default_factory=list)
