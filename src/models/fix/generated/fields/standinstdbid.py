"""
FIX StandInstDbID field (tag 171).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class StandInstDbIDField(FIXFieldBase):
    """"""
    tag: str = "171"
    name: str = "StandInstDbID"
    type: str = "STRING"
    value: str
