"""
FIX 4.4 SettlInstructionsData Component

This module contains the Pydantic model for the SettlInstructionsData component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class SettlInstructionsData(TradeModel):
    """
    FIX 4.4 SettlInstructionsData Component
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
    SettlDeliveryType: Optional[int] = Field(None, description='', alias='172')
    StandInstDbType: Optional[int] = Field(None, description='', alias='169')
    StandInstDbName: Optional[str] = Field(None, description='', alias='170')
    StandInstDbID: Optional[str] = Field(None, description='', alias='171')
    DlvyInstGrp: Optional[str] = Field(None)
