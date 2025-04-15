"""
FIX Component Model - AffectedOrdGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoAffectedOrdersGroup(FIXComponentBase):

    """FIX Group - NoAffectedOrders"""

    OrigClOrdID: Optional[str] = Field(None, alias='41', description='')
    AffectedOrderID: Optional[str] = Field(None, alias='535', description='')
    AffectedSecondaryOrderID: Optional[str] = Field(None, alias='536', description='')



class AffectedOrdGrpComponent(FIXComponentBase):
    """FIX Component - AffectedOrdGrp"""


