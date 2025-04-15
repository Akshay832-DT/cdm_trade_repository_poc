"""
FIX OnBehalfOfLocationID field (tag 144).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OnBehalfOfLocationIDField(FIXFieldBase):
    """"""
    tag: str = "144"
    name: str = "OnBehalfOfLocationID"
    type: str = "STRING"
    value: str
