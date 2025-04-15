"""
FIX CollRespID field (tag 904).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CollRespIDField(FIXFieldBase):
    """"""
    tag: str = "904"
    name: str = "CollRespID"
    type: str = "STRING"
    value: str
