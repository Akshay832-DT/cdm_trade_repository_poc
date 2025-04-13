"""
FIX 4.4 DlvyInstGrp Component

This module contains the Pydantic model for the DlvyInstGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoDlvyInstGroup(FIXComponentBase):
    """
    NoDlvyInst group fields
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
    
    SettlInstSource: Optional[str] = Field(None, description='', alias='165')
    DlvyInstType: Optional[str] = Field(None, description='', alias='787')


class DlvyInstGrpComponent(FIXComponentBase):
    """
    FIX 4.4 DlvyInstGrp Component
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
    
    SettlParties: Optional[SettlPartiesComponent] = Field(None, description='SettlParties component')
    NoDlvyInst: Optional[int] = Field(None, description='Number of NoDlvyInst entries', alias='')
    NoDlvyInst_items: List[NoDlvyInstGroup] = Field(default_factory=list)
