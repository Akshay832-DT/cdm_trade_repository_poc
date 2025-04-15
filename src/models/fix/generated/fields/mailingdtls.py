"""
FIX MailingDtls field (tag 474).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MailingDtlsField(FIXFieldBase):
    """"""
    tag: str = "474"
    name: str = "MailingDtls"
    type: str = "STRING"
    value: str
