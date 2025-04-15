"""
FIX CollAsgnRefID field (tag 907).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CollAsgnRefIDField(FIXFieldBase):
    """"""
    tag: str = "907"
    name: str = "CollAsgnRefID"
    type: str = "STRING"
    value: str
