"""
FIX Component Model - Hop
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoHopsGroup(FIXComponentBase):

    """FIX Group - NoHops"""

    HopCompID: Optional[str] = Field(None, alias='628', description='')
    HopSendingTime: Optional[datetime] = Field(None, alias='629', description='')
    HopRefID: Optional[int] = Field(None, alias='630', description='')



class HopComponent(FIXComponentBase):
    """FIX Component - Hop"""


