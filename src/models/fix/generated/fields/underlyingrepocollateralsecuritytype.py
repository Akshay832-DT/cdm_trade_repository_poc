"""
FIX UnderlyingRepoCollateralSecurityType field (tag 243).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingRepoCollateralSecurityTypeField(FIXFieldBase):
    """"""
    tag: str = "243"
    name: str = "UnderlyingRepoCollateralSecurityType"
    type: str = "STRING"
    value: str
