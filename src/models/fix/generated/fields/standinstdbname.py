"""
FIX StandInstDbName field (tag 170).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class StandInstDbNameField(FIXFieldBase):
    """"""
    tag: str = "170"
    name: str = "StandInstDbName"
    type: str = "STRING"
    value: str
