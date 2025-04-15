"""
FIX SecurityAltID field (tag 455).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SecurityAltIDField(FIXFieldBase):
    """"""
    tag: str = "455"
    name: str = "SecurityAltID"
    type: str = "STRING"
    value: str
