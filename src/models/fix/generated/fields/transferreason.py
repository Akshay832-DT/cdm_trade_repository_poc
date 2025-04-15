"""
FIX TransferReason field (tag 830).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TransferReasonField(FIXFieldBase):
    """"""
    tag: str = "830"
    name: str = "TransferReason"
    type: str = "STRING"
    value: str
