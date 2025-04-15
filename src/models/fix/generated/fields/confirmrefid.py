"""
FIX ConfirmRefID field (tag 772).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ConfirmRefIDField(FIXFieldBase):
    """"""
    tag: str = "772"
    name: str = "ConfirmRefID"
    type: str = "STRING"
    value: str
