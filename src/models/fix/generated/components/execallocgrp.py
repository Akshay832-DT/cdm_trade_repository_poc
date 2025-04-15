"""
FIX Component Model - ExecAllocGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoExecsGroup(FIXComponentBase):

    """FIX Group - NoExecs"""

    LastQty: Optional[float] = Field(None, alias='32', description='')
    ExecID: Optional[str] = Field(None, alias='17', description='')
    SecondaryExecID: Optional[str] = Field(None, alias='527', description='')
    LastPx: Optional[float] = Field(None, alias='31', description='')
    LastParPx: Optional[float] = Field(None, alias='669', description='')
    LastCapacity: Optional[str] = Field(None, alias='29', description='')



class ExecAllocGrpComponent(FIXComponentBase):
    """FIX Component - ExecAllocGrp"""


