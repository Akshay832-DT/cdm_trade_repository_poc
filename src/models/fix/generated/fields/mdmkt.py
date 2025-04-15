"""
FIX MDMkt field (tag 275).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MDMktField(FIXFieldBase):
    """"""
    tag: str = "275"
    name: str = "MDMkt"
    type: str = "EXCHANGE"
    value: str
