"""
FIX NoCollInquiryQualifier field (tag 938).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoCollInquiryQualifierField(FIXFieldBase):
    """"""
    tag: str = "938"
    name: str = "NoCollInquiryQualifier"
    type: str = "NUMINGROUP"
    value: int
