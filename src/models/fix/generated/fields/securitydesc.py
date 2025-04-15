"""
FIX SecurityDesc field (tag 107).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SecurityDescField(FIXFieldBase):
    """"""
    tag: str = "107"
    name: str = "SecurityDesc"
    type: str = "STRING"
    value: str
