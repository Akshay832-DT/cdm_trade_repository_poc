"""
FIX AsgnRptID field (tag 833).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AsgnRptIDField(FIXFieldBase):
    """"""
    tag: str = "833"
    name: str = "AsgnRptID"
    type: str = "STRING"
    value: str
