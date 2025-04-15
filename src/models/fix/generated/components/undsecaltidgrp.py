"""
FIX Component Model - UndSecAltIDGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoUnderlyingSecurityAltIDGroup(FIXComponentBase):

    """FIX Group - NoUnderlyingSecurityAltID"""

    UnderlyingSecurityAltID: Optional[str] = Field(None, alias='458', description='')
    UnderlyingSecurityAltIDSource: Optional[str] = Field(None, alias='459', description='')



class UndSecAltIDGrpComponent(FIXComponentBase):
    """FIX Component - UndSecAltIDGrp"""


