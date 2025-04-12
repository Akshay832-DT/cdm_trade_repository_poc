"""
FIX 4.4 DlvyInstGrp Component

This module contains the Pydantic model for the DlvyInstGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class DlvyInstGrp(TradeModel):
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
    SettlInstSource: Optional[str] = Field(None, description='', alias='165')
    DlvyInstType: Optional[str] = Field(None, description='', alias='787')
    SettlParties: Optional[str] = Field(None)


class NoDlvyInst(TradeModel):
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

    NoDlvyInsts: List[NoDlvyInst] = Field(default_factory=list)
