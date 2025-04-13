"""
FIX 4.4 RgstDistInstGrp Component

This module contains the Pydantic model for the RgstDistInstGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class NoDistribInsts(FIXMessageBase):
    """
    NoDistribInsts group fields
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
    
    distribPaymentMethod: Optional[int] = Field(None, description='', alias='477')
    distribPercentage: Optional[float] = Field(None, description='', alias='512')
    cashDistribCurr: Optional[str] = Field(None, description='', alias='478')
    cashDistribAgentName: Optional[str] = Field(None, description='', alias='498')
    cashDistribAgentCode: Optional[str] = Field(None, description='', alias='499')
    cashDistribAgentAcctNumber: Optional[str] = Field(None, description='', alias='500')
    cashDistribPayRef: Optional[str] = Field(None, description='', alias='501')
    cashDistribAgentAcctName: Optional[str] = Field(None, description='', alias='502')


class RgstDistInstGrp(FIXMessageBase):
    """
    FIX 4.4 RgstDistInstGrp Component
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
    
    noDistribInsts: Optional[int] = Field(None, description='Number of NoDistribInsts entries', alias='510')
    noDistribInsts_items: List[NoDistribInsts] = Field(default_factory=list)
