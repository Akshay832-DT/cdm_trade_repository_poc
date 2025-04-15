"""
FIX TrdRegTimestampOrigin field (tag 771).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TrdRegTimestampOriginField(FIXFieldBase):
    """"""
    tag: str = "771"
    name: str = "TrdRegTimestampOrigin"
    type: str = "STRING"
    value: str
