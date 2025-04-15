"""
FIX ApplQueueDepth field (tag 813).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ApplQueueDepthField(FIXFieldBase):
    """"""
    tag: str = "813"
    name: str = "ApplQueueDepth"
    type: str = "INT"
    value: int
