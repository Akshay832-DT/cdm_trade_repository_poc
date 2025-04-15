"""
FIX LegSecurityID field (tag 602).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegSecurityIDField(FIXFieldBase):
    """"""
    tag: str = "602"
    name: str = "LegSecurityID"
    type: str = "STRING"
    value: str
