"""
FIX Component Model - LegSecAltIDGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoLegSecurityAltIDGroup(FIXComponentBase):

    """FIX Group - NoLegSecurityAltID"""

    LegSecurityAltID: Optional[str] = Field(None, alias='605', description='')
    LegSecurityAltIDSource: Optional[str] = Field(None, alias='606', description='')



class LegSecAltIDGrpComponent(FIXComponentBase):
    """FIX Component - LegSecAltIDGrp"""


