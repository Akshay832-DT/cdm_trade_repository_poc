"""
FIX OnBehalfOfCompID field (tag 115).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OnBehalfOfCompIDField(FIXFieldBase):
    """"""
    tag: str = "115"
    name: str = "OnBehalfOfCompID"
    type: str = "STRING"
    value: str
