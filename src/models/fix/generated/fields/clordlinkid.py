"""
FIX ClOrdLinkID field (tag 583).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ClOrdLinkIDField(FIXFieldBase):
    """"""
    tag: str = "583"
    name: str = "ClOrdLinkID"
    type: str = "STRING"
    value: str
