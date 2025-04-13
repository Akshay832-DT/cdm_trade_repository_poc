"""
FIX 4.4 QuotCxlEntriesGrp Component

This module contains the Pydantic model for the QuotCxlEntriesGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoQuoteEntriesGroup(FIXComponentBase):
    """
    NoQuoteEntries group fields
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
    


class QuotCxlEntriesGrpComponent(FIXComponentBase):
    """
    FIX 4.4 QuotCxlEntriesGrp Component
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
    
    Instrument: Optional[InstrumentComponent] = Field(None, description='Instrument component')
    FinancingDetails: Optional[FinancingDetailsComponent] = Field(None, description='FinancingDetails component')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='UndInstrmtGrp component')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='InstrmtLegGrp component')
    NoQuoteEntries: Optional[int] = Field(None, description='Number of NoQuoteEntries entries', alias='')
    NoQuoteEntries_items: List[NoQuoteEntriesGroup] = Field(default_factory=list)
