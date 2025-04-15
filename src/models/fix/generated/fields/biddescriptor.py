"""
FIX BidDescriptor field (tag 400).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class BidDescriptorField(FIXFieldBase):
    """"""
    tag: str = "400"
    name: str = "BidDescriptor"
    type: str = "STRING"
    value: str
