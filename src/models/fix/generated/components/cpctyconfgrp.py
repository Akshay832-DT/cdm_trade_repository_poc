"""
FIX Component Model - CpctyConfGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoCapacitiesGroup(FIXComponentBase):

    """FIX Group - NoCapacities"""

    OrderCapacity: str = Field(alias='528', description='')
    OrderRestrictions: Optional[str] = Field(None, alias='529', description='')
    OrderCapacityQty: float = Field(alias='863', description='')



class CpctyConfGrpComponent(FIXComponentBase):
    """FIX Component - CpctyConfGrp"""


