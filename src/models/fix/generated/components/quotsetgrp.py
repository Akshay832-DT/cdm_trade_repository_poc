"""
FIX 4.4 QuotSetGrp Component

This module contains the Pydantic model for the QuotSetGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoQuoteSetsGroup(FIXComponentBase):
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
    
    QuoteSetID: str = Field(..., description='', alias='302')
    QuoteSetValidUntilTime: Optional[datetime] = Field(None, description='', alias='367')
    TotNoQuoteEntries: int = Field(..., description='', alias='304')
    LastFragment: Optional[bool] = Field(None, description='', alias='893')


class QuotSetGrpComponent(FIXComponentBase):
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
    
    UnderlyingInstrument: Optional[UnderlyingInstrumentComponent] = Field(None, description='UnderlyingInstrument component')
    QuotEntryGrp: QuotEntryGrpComponent = Field(..., description='QuotEntryGrp component')
    NoQuoteSets: Optional[int] = Field(None, description='Number of NoQuoteSets entries', alias='')
    NoQuoteSets_items: List[NoQuoteSetsGroup] = Field(default_factory=list)
