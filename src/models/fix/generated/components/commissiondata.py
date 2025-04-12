"""
FIX 4.4 CommissionData Component

This module contains the Pydantic model for the CommissionData component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class CommissionData(FIXMessageBase):
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
    commission: Optional[float] = Field(None, description='', alias='12')
    commType: Optional[str] = Field(None, description='', alias='13')
    commCurrency: Optional[str] = Field(None, description='', alias='479')
    fundRenewWaiv: Optional[str] = Field(None, description='', alias='497')
