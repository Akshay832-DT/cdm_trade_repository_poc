"""
FIX BenchmarkSecurityID field (tag 699).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class BenchmarkSecurityIDField(FIXFieldBase):
    """"""
    tag: str = "699"
    name: str = "BenchmarkSecurityID"
    type: str = "STRING"
    value: str
