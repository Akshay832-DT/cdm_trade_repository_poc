"""
FIX Component Model - SecAltIDGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoSecurityAltIDGroup(FIXComponentBase):

    """FIX Group - NoSecurityAltID"""

    SecurityAltID: Optional[str] = Field(None, alias='455', description='')
    SecurityAltIDSource: Optional[str] = Field(None, alias='456', description='')



class SecAltIDGrpComponent(FIXComponentBase):
    """FIX Component - SecAltIDGrp"""


