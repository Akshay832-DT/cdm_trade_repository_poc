"""
FIX ClientBidID field (tag 391).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ClientBidIDField(FIXFieldBase):
    """"""
    tag: str = "391"
    name: str = "ClientBidID"
    type: str = "STRING"
    value: str
