"""
FIX SettlPartySubIDType field (tag 786).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SettlPartySubIDTypeField(FIXFieldBase):
    """"""
    tag: str = "786"
    name: str = "SettlPartySubIDType"
    type: str = "INT"
    value: int
