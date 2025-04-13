"""
FIX 4.4 SecTypesGrp Component

This module contains the Pydantic model for the SecTypesGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoSecurityTypesGroup(FIXComponentBase):
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


class SecTypesGrpComponent(FIXComponentBase):
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
    
    NoSecurityTypes: Optional[int] = Field(None, description='Number of NoSecurityTypes entries', alias='')
    NoSecurityTypes_items: List[NoSecurityTypesGroup] = Field(default_factory=list)
