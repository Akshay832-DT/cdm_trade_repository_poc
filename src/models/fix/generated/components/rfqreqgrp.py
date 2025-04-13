"""
FIX 4.4 RFQReqGrp Component

This module contains the Pydantic model for the RFQReqGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp


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
    
    prevClosePx: Optional[float] = Field(None, description='', alias='140')
    quoteRequestType: Optional[int] = Field(None, description='', alias='303')
    quoteType: Optional[int] = Field(None, description='', alias='537')
    tradingSessionID: Optional[str] = Field(None, description='', alias='336')
    tradingSessionSubID: Optional[str] = Field(None, description='', alias='625')


class RFQReqGrp(FIXMessageBase):
    """
    FIX 4.4 RFQReqGrp Component
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
    
    instrument: Instrument = Field(..., description='Instrument component')
    undInstrmtGrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    instrmtLegGrp: Optional[InstrmtLegGrp] = Field(None, description='InstrmtLegGrp component')
    noRelatedSym: Optional[int] = Field(None, description='Number of NoRelatedSym entries', alias='146')
    noRelatedSym_items: List[NoRelatedSym] = Field(default_factory=list)
