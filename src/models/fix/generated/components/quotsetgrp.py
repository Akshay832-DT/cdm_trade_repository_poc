"""
FIX 4.4 QuotSetGrp Component

This module contains the Pydantic model for the QuotSetGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


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
    quoteSetID: str = Field(None, description='', alias='302')
    quoteSetValidUntilTime: Optional[datetime] = Field(None, description='', alias='367')
    totNoQuoteEntries: int = Field(None, description='', alias='304')
    lastFragment: Optional[bool] = Field(None, description='', alias='893')
    underlyingInstrument: Optional[str] = Field(None)
    quotEntryGrp: str = Field(None)


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
    quoteSetID: int = Field(None, description='', alias='296')
    quoteSetValidUntilTime: Optional[int] = Field(None, description='', alias='296')
    totNoQuoteEntries: int = Field(None, description='', alias='296')
    lastFragment: Optional[int] = Field(None, description='', alias='296')

    noQuoteSetss: List[NoQuoteSets] = Field(default_factory=list)
