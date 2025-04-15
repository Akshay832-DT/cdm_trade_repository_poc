"""
FIX BenchmarkSecurityIDSource field (tag 761).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class BenchmarkSecurityIDSourceField(FIXFieldBase):
    """"""
    tag: str = "761"
    name: str = "BenchmarkSecurityIDSource"
    type: str = "STRING"
    value: str
