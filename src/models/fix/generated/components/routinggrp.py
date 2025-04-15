"""
FIX Component Model - RoutingGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoRoutingIDsGroup(FIXComponentBase):

    """FIX Group - NoRoutingIDs"""

    RoutingType: Optional[int] = Field(None, alias='216', description='')
    RoutingID: Optional[str] = Field(None, alias='217', description='')



class RoutingGrpComponent(FIXComponentBase):
    """FIX Component - RoutingGrp"""


