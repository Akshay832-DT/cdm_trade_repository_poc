"""
FIX CollInquiryID field (tag 909).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CollInquiryIDField(FIXFieldBase):
    """"""
    tag: str = "909"
    name: str = "CollInquiryID"
    type: str = "STRING"
    value: str
