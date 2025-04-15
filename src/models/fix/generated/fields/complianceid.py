"""
FIX ComplianceID field (tag 376).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ComplianceIDField(FIXFieldBase):
    """"""
    tag: str = "376"
    name: str = "ComplianceID"
    type: str = "STRING"
    value: str
