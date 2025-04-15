"""
FIX LegSecuritySubType field (tag 764).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegSecuritySubTypeField(FIXFieldBase):
    """"""
    tag: str = "764"
    name: str = "LegSecuritySubType"
    type: str = "STRING"
    value: str
