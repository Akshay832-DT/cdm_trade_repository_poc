"""
FIX Component Model - PegInstructions
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List




class PegInstructionsComponent(FIXComponentBase):
    """FIX Component - PegInstructions"""
    PegOffsetValue: Optional[float] = Field(None, alias='211', description='')
    PegMoveType: Optional[int] = Field(None, alias='835', description='')
    PegOffsetType: Optional[int] = Field(None, alias='836', description='')
    PegLimitType: Optional[int] = Field(None, alias='837', description='')
    PegRoundDirection: Optional[int] = Field(None, alias='838', description='')
    PegScope: Optional[int] = Field(None, alias='840', description='')

