"""
FIX AffectedOrderID field (tag 535).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AffectedOrderIDField(FIXFieldBase):
    """"""
    tag: str = "535"
    name: str = "AffectedOrderID"
    type: str = "STRING"
    value: str
