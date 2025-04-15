"""
FIX LastNetworkResponseID field (tag 934).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LastNetworkResponseIDField(FIXFieldBase):
    """"""
    tag: str = "934"
    name: str = "LastNetworkResponseID"
    type: str = "STRING"
    value: str
