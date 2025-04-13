"""
FIX 4.4 SettlInstructionsData Component

This module contains the Pydantic model for the SettlInstructionsData component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.dlvyinstgrp import DlvyInstGrp


class SettlInstructionsData(FIXMessageBase):
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
    
    settlDeliveryType: Optional[int] = Field(None, description='', alias='172')
    standInstDbType: Optional[int] = Field(None, description='', alias='169')
    standInstDbName: Optional[str] = Field(None, description='', alias='170')
    standInstDbID: Optional[str] = Field(None, description='', alias='171')
    dlvyInstGrp: Optional[DlvyInstGrp] = Field(None, description='DlvyInstGrp component')
