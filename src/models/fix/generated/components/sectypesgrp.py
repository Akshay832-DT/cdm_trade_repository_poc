"""
FIX 4.4 SecTypesGrp Component

This module contains the Pydantic model for the SecTypesGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class SecTypesGrp(TradeModel):
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
    SecurityType: Optional[str] = Field(None, description='', alias='167')
    SecuritySubType: Optional[str] = Field(None, description='', alias='762')
    Product: Optional[int] = Field(None, description='', alias='460')
    CFICode: Optional[str] = Field(None, description='', alias='461')


class NoSecurityTypes(TradeModel):
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
    SecurityType: Optional[str] = Field(None, description='', alias='167')
    SecuritySubType: Optional[str] = Field(None, description='', alias='762')
    Product: Optional[int] = Field(None, description='', alias='460')
    CFICode: Optional[str] = Field(None, description='', alias='461')

    NoSecurityTypess: List[NoSecurityTypes] = Field(default_factory=list)
