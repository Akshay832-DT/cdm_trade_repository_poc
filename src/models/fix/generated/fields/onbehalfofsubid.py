"""
FIX OnBehalfOfSubID field (tag 116).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OnBehalfOfSubIDField(FIXFieldBase):
    """"""
    tag: str = "116"
    name: str = "OnBehalfOfSubID"
    type: str = "STRING"
    value: str
