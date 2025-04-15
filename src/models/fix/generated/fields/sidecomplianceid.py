"""
FIX SideComplianceID field (tag 659).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SideComplianceIDField(FIXFieldBase):
    """"""
    tag: str = "659"
    name: str = "SideComplianceID"
    type: str = "STRING"
    value: str
