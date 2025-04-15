"""
FIX MDReqID field (tag 262).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MDReqIDField(FIXFieldBase):
    """"""
    tag: str = "262"
    name: str = "MDReqID"
    type: str = "STRING"
    value: str
