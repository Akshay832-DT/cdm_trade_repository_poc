"""
FIX NetworkResponseID field (tag 932).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NetworkResponseIDField(FIXFieldBase):
    """"""
    tag: str = "932"
    name: str = "NetworkResponseID"
    type: str = "STRING"
    value: str
