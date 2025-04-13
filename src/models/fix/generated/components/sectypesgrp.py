"""
FIX 4.4 SecTypesGrp Component

This module contains the Pydantic model for the SecTypesGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class NoSecurityTypes(FIXMessageBase):
    """
    NoSecurityTypes group fields
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
    
    securityType: Optional[str] = Field(None, description='', alias='167')
    securitySubType: Optional[str] = Field(None, description='', alias='762')
    product: Optional[int] = Field(None, description='', alias='460')
    cFICode: Optional[str] = Field(None, description='', alias='461')


class SecTypesGrp(FIXMessageBase):
    """
    FIX 4.4 SecTypesGrp Component
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
    
    noSecurityTypes: Optional[int] = Field(None, description='Number of NoSecurityTypes entries', alias='558')
    noSecurityTypes_items: List[NoSecurityTypes] = Field(default_factory=list)
