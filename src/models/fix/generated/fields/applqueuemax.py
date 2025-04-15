"""
FIX ApplQueueMax field (tag 812).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ApplQueueMaxField(FIXFieldBase):
    """"""
    tag: str = "812"
    name: str = "ApplQueueMax"
    type: str = "INT"
    value: int
