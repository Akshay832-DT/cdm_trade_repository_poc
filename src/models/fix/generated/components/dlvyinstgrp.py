"""
FIX Component Model - DlvyInstGrp
"""

from ..base import FIXComponentBase
from .settlparties import SettlPartiesComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoDlvyInstGroup(FIXComponentBase):

    """FIX Group - NoDlvyInst"""

    SettlInstSource: Optional[str] = Field(None, alias='165', description='')
    DlvyInstType: Optional[str] = Field(None, alias='787', description='')
    SettlParties: Optional[SettlPartiesComponent] = Field(None, description='')



class DlvyInstGrpComponent(FIXComponentBase):
    """FIX Component - DlvyInstGrp"""


