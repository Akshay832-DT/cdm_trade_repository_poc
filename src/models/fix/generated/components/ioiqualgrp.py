"""
FIX Component Model - IOIQualGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoIOIQualifiersGroup(FIXComponentBase):

    """FIX Group - NoIOIQualifiers"""

    IOIQualifier: Optional[str] = Field(None, alias='104', description='')



class IOIQualGrpComponent(FIXComponentBase):
    """FIX Component - IOIQualGrp"""


