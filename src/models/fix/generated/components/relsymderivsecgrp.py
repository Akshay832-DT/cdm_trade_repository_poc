"""
FIX 4.4 RelSymDerivSecGrp Component

This module contains the Pydantic model for the RelSymDerivSecGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.instrumentextension import InstrumentExtension
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
    
    currency: Optional[str] = Field(None, description='', alias='15')
    expirationCycle: Optional[int] = Field(None, description='', alias='827')
    tradingSessionID: Optional[str] = Field(None, description='', alias='336')
    tradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')


class RelSymDerivSecGrp(FIXMessageBase):
    """
    FIX 4.4 RelSymDerivSecGrp Component
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
    
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    instrumentExtension: Optional[InstrumentExtension] = Field(None, description='InstrumentExtension component')
    instrmtLegGrp: Optional[InstrmtLegGrp] = Field(None, description='InstrmtLegGrp component')
    noRelatedSym: Optional[int] = Field(None, description='Number of NoRelatedSym entries', alias='146')
    noRelatedSym_items: List[NoRelatedSym] = Field(default_factory=list)
