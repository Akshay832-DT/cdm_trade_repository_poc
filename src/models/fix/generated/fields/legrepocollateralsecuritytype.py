"""
FIX LegRepoCollateralSecurityType field (tag 250).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegRepoCollateralSecurityTypeField(FIXFieldBase):
    """"""
    tag: str = "250"
    name: str = "LegRepoCollateralSecurityType"
    type: str = "STRING"
    value: str
