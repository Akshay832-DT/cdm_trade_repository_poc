"""
FIX Component Model - CompIDReqGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoCompIDsGroup(FIXComponentBase):

    """FIX Group - NoCompIDs"""

    RefCompID: Optional[str] = Field(None, alias='930', description='')
    RefSubID: Optional[str] = Field(None, alias='931', description='')
    LocationID: Optional[str] = Field(None, alias='283', description='')
    DeskID: Optional[str] = Field(None, alias='284', description='')



class CompIDReqGrpComponent(FIXComponentBase):
    """FIX Component - CompIDReqGrp"""


