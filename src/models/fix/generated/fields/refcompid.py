"""
FIX RefCompID field (tag 930).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class RefCompIDField(FIXFieldBase):
    """"""
    tag: str = "930"
    name: str = "RefCompID"
    type: str = "STRING"
    value: str
