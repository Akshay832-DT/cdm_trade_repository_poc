"""
FIX SecuritySubType field (tag 762).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SecuritySubTypeField(FIXFieldBase):
    """"""
    tag: str = "762"
    name: str = "SecuritySubType"
    type: str = "STRING"
    value: str
