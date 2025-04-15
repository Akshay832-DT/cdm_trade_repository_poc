"""
FIX Component Model - SettlInstructionsData
"""

from ..base import FIXComponentBase
from .dlvyinstgrp import DlvyInstGrpComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List




class SettlInstructionsDataComponent(FIXComponentBase):
    """FIX Component - SettlInstructionsData"""
    SettlDeliveryType: Optional[int] = Field(None, alias='172', description='')
    StandInstDbType: Optional[int] = Field(None, alias='169', description='')
    StandInstDbName: Optional[str] = Field(None, alias='170', description='')
    StandInstDbID: Optional[str] = Field(None, alias='171', description='')
    DlvyInstGrp: Optional[DlvyInstGrpComponent] = Field(None, description='')

