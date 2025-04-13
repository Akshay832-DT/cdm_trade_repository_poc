"""
FIX 4.4 CommissionData Component

This module contains the Pydantic model for the CommissionData component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class CommissionDataComponent(FIXComponentBase):
    """
    FIX 4.4 CommissionData Component
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
    
    Commission: Optional[float] = Field(None, description='', alias='12')
    CommType: Optional[str] = Field(None, description='', alias='13')
    CommCurrency: Optional[str] = Field(None, description='', alias='479')
    FundRenewWaiv: Optional[str] = Field(None, description='', alias='497')
