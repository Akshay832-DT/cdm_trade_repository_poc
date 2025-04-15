"""
FIX ListName field (tag 392).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ListNameField(FIXFieldBase):
    """"""
    tag: str = "392"
    name: str = "ListName"
    type: str = "STRING"
    value: str
