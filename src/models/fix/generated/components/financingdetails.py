"""
FIX 4.4 FinancingDetails Component

This module contains the Pydantic model for the FinancingDetails component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class FinancingDetails(FIXMessageBase):
    """
    FIX 4.4 FinancingDetails Component
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
    
    agreementDesc: Optional[str] = Field(None, description='', alias='913')
    agreementID: Optional[str] = Field(None, description='', alias='914')
    agreementDate: Optional[date] = Field(None, description='', alias='915')
    agreementCurrency: Optional[str] = Field(None, description='', alias='918')
    terminationType: Optional[int] = Field(None, description='', alias='788')
    startDate: Optional[date] = Field(None, description='', alias='916')
    endDate: Optional[date] = Field(None, description='', alias='917')
    deliveryType: Optional[int] = Field(None, description='', alias='919')
    marginRatio: Optional[float] = Field(None, description='', alias='898')
