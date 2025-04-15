"""
FIX Component Model - ExecsGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoExecsGroup(FIXComponentBase):

    """FIX Group - NoExecs"""

    ExecID: Optional[str] = Field(None, alias='17', description='')



class ExecsGrpComponent(FIXComponentBase):
    """FIX Component - ExecsGrp"""


