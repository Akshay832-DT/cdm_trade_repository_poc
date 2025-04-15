"""
FIX TradSesReqID field (tag 335).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TradSesReqIDField(FIXFieldBase):
    """"""
    tag: str = "335"
    name: str = "TradSesReqID"
    type: str = "STRING"
    value: str
