"""
FIX LastMkt field (tag 30).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LastMktField(FIXFieldBase):
    """"""
    tag: str = "30"
    name: str = "LastMkt"
    type: str = "EXCHANGE"
    value: str
