"""
FIX 4.4 FinancingDetails Component

This module contains the Pydantic model for the FinancingDetails component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class FinancingDetailsComponent(FIXComponentBase):
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
    
    AgreementDesc: Optional[str] = Field(None, description='', alias='913')
    AgreementID: Optional[str] = Field(None, description='', alias='914')
    AgreementDate: Optional[date] = Field(None, description='', alias='915')
    AgreementCurrency: Optional[str] = Field(None, description='', alias='918')
    TerminationType: Optional[int] = Field(None, description='', alias='788')
    StartDate: Optional[date] = Field(None, description='', alias='916')
    EndDate: Optional[date] = Field(None, description='', alias='917')
    DeliveryType: Optional[int] = Field(None, description='', alias='919')
    MarginRatio: Optional[float] = Field(None, description='', alias='898')
