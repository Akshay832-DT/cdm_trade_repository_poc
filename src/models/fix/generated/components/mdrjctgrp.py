"""
FIX Component Model - MDRjctGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoAltMDSourceGroup(FIXComponentBase):

    """FIX Group - NoAltMDSource"""

    AltMDSourceID: Optional[str] = Field(None, alias='817', description='')



class MDRjctGrpComponent(FIXComponentBase):
    """FIX Component - MDRjctGrp"""


