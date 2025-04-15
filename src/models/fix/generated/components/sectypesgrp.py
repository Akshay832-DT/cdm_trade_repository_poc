"""
FIX Component Model - SecTypesGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoSecurityTypesGroup(FIXComponentBase):

    """FIX Group - NoSecurityTypes"""

    SecurityType: Optional[str] = Field(None, alias='167', description='')
    SecuritySubType: Optional[str] = Field(None, alias='762', description='')
    Product: Optional[int] = Field(None, alias='460', description='')
    CFICode: Optional[str] = Field(None, alias='461', description='')



class SecTypesGrpComponent(FIXComponentBase):
    """FIX Component - SecTypesGrp"""


