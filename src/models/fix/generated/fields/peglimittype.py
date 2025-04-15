"""
FIX PegLimitType field (tag 837).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PegLimitTypeValues:
    """Enumerated values for PegLimitType."""
    VALUE_0 = "0"  # OR_BETTER
    VALUE_1 = "1"  # STRICT
    VALUE_2 = "2"  # OR_WORSE

class PegLimitTypeField(FIXFieldBase):
    """"""
    tag: str = "837"
    name: str = "PegLimitType"
    type: str = "INT"
    value: Literal["0", "1", "2"]

    # Helper methods for enum values
    @property
    def is_value_0(self) -> bool:
        return self.value == "0"
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
    @property
    def is_value_2(self) -> bool:
        return self.value == "2"
