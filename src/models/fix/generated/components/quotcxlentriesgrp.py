"""
FIX 4.4 QuotCxlEntriesGrp Component

This module contains the Pydantic model for the QuotCxlEntriesGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.financingdetails import FinancingDetails
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp


class NoQuoteEntries(FIXMessageBase):
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
    


class QuotCxlEntriesGrp(FIXMessageBase):
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
    
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    financingDetails: Optional[FinancingDetails] = Field(None, description='FinancingDetails component')
    undInstrmtGrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    instrmtLegGrp: Optional[InstrmtLegGrp] = Field(None, description='InstrmtLegGrp component')
    noQuoteEntries: Optional[int] = Field(None, description='Number of NoQuoteEntries entries', alias='295')
    noQuoteEntries_items: List[NoQuoteEntries] = Field(default_factory=list)
