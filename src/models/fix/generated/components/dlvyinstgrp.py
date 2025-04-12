"""
FIX 4.4 DlvyInstGrp Component

This module contains the Pydantic model for the DlvyInstGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class DlvyInstGrp(FIXMessageBase):
    """
    FIX 4.4 DlvyInstGrp Component
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
    settlInstSource: Optional[str] = Field(None, description='', alias='165')
    dlvyInstType: Optional[str] = Field(None, description='', alias='787')
    settlParties: Optional[str] = Field(None)


class NoDlvyInst(FIXMessageBase):
    """
    NoDlvyInst group fields
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
    settlInstSource: Optional[int] = Field(None, description='', alias='85')
    dlvyInstType: Optional[int] = Field(None, description='', alias='85')

    noDlvyInsts: List[NoDlvyInst] = Field(default_factory=list)
