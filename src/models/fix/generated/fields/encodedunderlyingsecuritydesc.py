"""
FIX EncodedUnderlyingSecurityDesc field (tag 365).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EncodedUnderlyingSecurityDescField(FIXFieldBase):
    """"""
    tag: str = "365"
    name: str = "EncodedUnderlyingSecurityDesc"
    type: str = "DATA"
    value: str
