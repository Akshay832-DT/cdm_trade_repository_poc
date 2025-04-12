"""
FIX 4.4 QuotSetAckGrp Component

This module contains the Pydantic model for the QuotSetAckGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class QuotSetAckGrp(TradeModel):
    """
    FIX 4.4 QuotSetAckGrp Component
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
    QuoteSetID: Optional[str] = Field(None, description='', alias='302')
    TotNoQuoteEntries: Optional[int] = Field(None, description='', alias='304')
    LastFragment: Optional[bool] = Field(None, description='', alias='893')
    UnderlyingInstrument: Optional[str] = Field(None)
    QuotEntryAckGrp: Optional[str] = Field(None)


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
    QuoteSetID: Optional[str] = Field(None, description='', alias='302')
    TotNoQuoteEntries: Optional[int] = Field(None, description='', alias='304')
    LastFragment: Optional[bool] = Field(None, description='', alias='893')

    NoQuoteSetss: List[NoQuoteSets] = Field(default_factory=list)
