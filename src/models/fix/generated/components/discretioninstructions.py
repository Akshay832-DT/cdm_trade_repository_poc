"""
FIX Component Model - DiscretionInstructions
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List




class DiscretionInstructionsComponent(FIXComponentBase):
    """FIX Component - DiscretionInstructions"""
    DiscretionInst: Optional[str] = Field(None, alias='388', description='')
    DiscretionOffsetValue: Optional[float] = Field(None, alias='389', description='')
    DiscretionMoveType: Optional[int] = Field(None, alias='841', description='')
    DiscretionOffsetType: Optional[int] = Field(None, alias='842', description='')
    DiscretionLimitType: Optional[int] = Field(None, alias='843', description='')
    DiscretionRoundDirection: Optional[int] = Field(None, alias='844', description='')
    DiscretionScope: Optional[int] = Field(None, alias='846', description='')

