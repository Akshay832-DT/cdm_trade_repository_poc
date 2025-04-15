"""
FIX ConfirmID field (tag 664).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ConfirmIDField(FIXFieldBase):
    """"""
    tag: str = "664"
    name: str = "ConfirmID"
    type: str = "STRING"
    value: str
