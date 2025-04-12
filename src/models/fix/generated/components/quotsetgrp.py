"""
FIX 4.4 QuotSetGrp Component

This module contains the Pydantic model for the QuotSetGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class QuotSetGrp(TradeModel):
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
    QuoteSetID: str = Field(None, description='', alias='302')
    QuoteSetValidUntilTime: Optional[datetime] = Field(None, description='', alias='367')
    TotNoQuoteEntries: int = Field(None, description='', alias='304')
    LastFragment: Optional[bool] = Field(None, description='', alias='893')
    UnderlyingInstrument: Optional[str] = Field(None)
    QuotEntryGrp: str = Field(None)


class NoQuoteSets(TradeModel):
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
    QuoteSetID: str = Field(None, description='', alias='302')
    QuoteSetValidUntilTime: Optional[datetime] = Field(None, description='', alias='367')
    TotNoQuoteEntries: int = Field(None, description='', alias='304')
    LastFragment: Optional[bool] = Field(None, description='', alias='893')

    NoQuoteSetss: List[NoQuoteSets] = Field(default_factory=list)
