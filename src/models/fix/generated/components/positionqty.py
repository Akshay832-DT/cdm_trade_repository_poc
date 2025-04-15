"""
FIX Component Model - PositionQty
"""

from ..base import FIXComponentBase
from .nestedparties import NestedPartiesComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoPositionsGroup(FIXComponentBase):

    """FIX Group - NoPositions"""

    PosType: Optional[str] = Field(None, alias='703', description='')
    LongQty: Optional[float] = Field(None, alias='704', description='')
    ShortQty: Optional[float] = Field(None, alias='705', description='')
    PosQtyStatus: Optional[int] = Field(None, alias='706', description='')
    NestedParties: Optional[NestedPartiesComponent] = Field(None, description='')



class PositionQtyComponent(FIXComponentBase):
    """FIX Component - PositionQty"""


