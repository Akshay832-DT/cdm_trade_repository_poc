"""
FIX Component Model - MDReqGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoMDEntryTypesGroup(FIXComponentBase):

    """FIX Group - NoMDEntryTypes"""

    MDEntryType: str = Field(alias='269', description='')



class MDReqGrpComponent(FIXComponentBase):
    """FIX Component - MDReqGrp"""


