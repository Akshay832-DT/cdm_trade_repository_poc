"""
FIX SecurityAltIDSource field (tag 456).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SecurityAltIDSourceField(FIXFieldBase):
    """"""
    tag: str = "456"
    name: str = "SecurityAltIDSource"
    type: str = "STRING"
    value: str
