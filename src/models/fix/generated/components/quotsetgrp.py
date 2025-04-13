"""
FIX 4.4 QuotSetGrp Component

This module contains the Pydantic model for the QuotSetGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.underlyinginstrument import UnderlyingInstrument
from src.models.fix.generated.components.quotentrygrp import QuotEntryGrp


class NoQuoteSets(FIXMessageBase):
    """
    NoQuoteSets group fields
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
    
    quoteSetID: str = Field(..., description='', alias='302')
    quoteSetValidUntilTime: Optional[datetime] = Field(None, description='', alias='367')
    totNoQuoteEntries: int = Field(..., description='', alias='304')
    lastFragment: Optional[bool] = Field(None, description='', alias='893')


class QuotSetGrp(FIXMessageBase):
    """
    FIX 4.4 QuotSetGrp Component
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
    
    underlyingInstrument: Optional[UnderlyingInstrument] = Field(None, description='UnderlyingInstrument component')
    quotEntryGrp: QuotEntryGrp = Field(..., description='QuotEntryGrp component')
    noQuoteSets: Optional[int] = Field(None, description='Number of NoQuoteSets entries', alias='296')
    noQuoteSets_items: List[NoQuoteSets] = Field(default_factory=list)
