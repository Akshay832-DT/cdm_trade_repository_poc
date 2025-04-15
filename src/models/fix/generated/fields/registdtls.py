"""
FIX RegistDtls field (tag 509).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class RegistDtlsField(FIXFieldBase):
    """"""
    tag: str = "509"
    name: str = "RegistDtls"
    type: str = "STRING"
    value: str
