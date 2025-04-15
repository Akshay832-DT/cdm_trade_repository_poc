"""
FIX SecurityReqID field (tag 320).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SecurityReqIDField(FIXFieldBase):
    """"""
    tag: str = "320"
    name: str = "SecurityReqID"
    type: str = "STRING"
    value: str
