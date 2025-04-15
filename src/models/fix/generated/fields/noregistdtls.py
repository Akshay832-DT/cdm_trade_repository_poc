"""
FIX NoRegistDtls field (tag 473).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoRegistDtlsField(FIXFieldBase):
    """"""
    tag: str = "473"
    name: str = "NoRegistDtls"
    type: str = "NUMINGROUP"
    value: int
