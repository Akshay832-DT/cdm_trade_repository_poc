"""
FIX Component Model - EvntGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoEventsGroup(FIXComponentBase):

    """FIX Group - NoEvents"""

    EventType: Optional[int] = Field(None, alias='865', description='')
    EventDate: Optional[date] = Field(None, alias='866', description='')
    EventPx: Optional[float] = Field(None, alias='867', description='')
    EventText: Optional[str] = Field(None, alias='868', description='')



class EvntGrpComponent(FIXComponentBase):
    """FIX Component - EvntGrp"""


