"""
FIX 4.4 ContAmtGrp Component

This module contains the Pydantic model for the ContAmtGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoContAmtsGroup(FIXComponentBase):
    """
    NoContAmts group fields
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
    
    ContAmtType: Optional[int] = Field(None, description='', alias='519')
    ContAmtValue: Optional[float] = Field(None, description='', alias='520')
    ContAmtCurr: Optional[str] = Field(None, description='', alias='521')


class ContAmtGrpComponent(FIXComponentBase):
    """
    FIX 4.4 ContAmtGrp Component
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
    
    NoContAmts: Optional[int] = Field(None, description='Number of NoContAmts entries', alias='')
    NoContAmts_items: List[NoContAmtsGroup] = Field(default_factory=list)
