"""
FIX Component Model - ExecCollGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoExecsGroup(FIXComponentBase):

    """FIX Group - NoExecs"""

    ExecID: Optional[str] = Field(None, alias='17', description='')



class ExecCollGrpComponent(FIXComponentBase):
    """FIX Component - ExecCollGrp"""


