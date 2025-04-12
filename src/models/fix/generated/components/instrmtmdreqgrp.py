"""
FIX 4.4 InstrmtMDReqGrp Component

This module contains the Pydantic model for the InstrmtMDReqGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class InstrmtMDReqGrp(FIXMessageBase):
    """
    FIX 4.4 InstrmtMDReqGrp Component
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
    instrument: str = Field(None)
    undInstrmtGrp: Optional[str] = Field(None)
    instrmtLegGrp: Optional[str] = Field(None)


class NoRelatedSym(FIXMessageBase):
    """
    NoRelatedSym group fields
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

    noRelatedSyms: List[NoRelatedSym] = Field(default_factory=list)
