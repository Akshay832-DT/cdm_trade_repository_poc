"""
FIX AllocLinkType field (tag 197).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AllocLinkTypeValues:
    """Enumerated values for AllocLinkType."""
    VALUE_0 = "0"  # FX_NETTING
    VALUE_1 = "1"  # FX_SWAP

class AllocLinkTypeField(FIXFieldBase):
    """"""
    tag: str = "197"
    name: str = "AllocLinkType"
    type: str = "INT"
    value: Literal["0", "1"]

    # Helper methods for enum values
    @property
    def is_value_0(self) -> bool:
        return self.value == "0"
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
