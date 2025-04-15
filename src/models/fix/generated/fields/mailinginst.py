"""
FIX MailingInst field (tag 482).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MailingInstField(FIXFieldBase):
    """"""
    tag: str = "482"
    name: str = "MailingInst"
    type: str = "STRING"
    value: str
