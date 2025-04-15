"""
FIX Component Model - TrdRegTimestamps
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoTrdRegTimestampsGroup(FIXComponentBase):

    """FIX Group - NoTrdRegTimestamps"""

    TrdRegTimestamp: Optional[datetime] = Field(None, alias='769', description='')
    TrdRegTimestampType: Optional[int] = Field(None, alias='770', description='')
    TrdRegTimestampOrigin: Optional[str] = Field(None, alias='771', description='')



class TrdRegTimestampsComponent(FIXComponentBase):
    """FIX Component - TrdRegTimestamps"""


