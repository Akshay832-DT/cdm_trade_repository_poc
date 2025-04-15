"""
FIX SecurityStatusReqID field (tag 324).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SecurityStatusReqIDField(FIXFieldBase):
    """"""
    tag: str = "324"
    name: str = "SecurityStatusReqID"
    type: str = "STRING"
    value: str
