"""
FIX URLLink field (tag 149).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class URLLinkField(FIXFieldBase):
    """"""
    tag: str = "149"
    name: str = "URLLink"
    type: str = "STRING"
    value: str
