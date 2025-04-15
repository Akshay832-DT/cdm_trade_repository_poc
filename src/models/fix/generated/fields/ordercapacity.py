"""
FIX OrderCapacity field (tag 528).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OrderCapacityValues:
    """Enumerated values for OrderCapacity."""
    A = "A"  # AGENCY
    G = "G"  # PROPRIETARY
    I = "I"  # INDIVIDUAL
    P = "P"  # PRINCIPAL
    R = "R"  # RISKLESS_PRINCIPAL
    W = "W"  # AGENT_FOR_OTHER_MEMBER

class OrderCapacityField(FIXFieldBase):
    """"""
    tag: str = "528"
    name: str = "OrderCapacity"
    type: str = "CHAR"
    value: Literal["A", "G", "I", "P", "R", "W"]

    # Helper methods for enum values
    @property
    def is_a(self) -> bool:
        return self.value == "A"
    @property
    def is_g(self) -> bool:
        return self.value == "G"
    @property
    def is_i(self) -> bool:
        return self.value == "I"
    @property
    def is_p(self) -> bool:
        return self.value == "P"
    @property
    def is_r(self) -> bool:
        return self.value == "R"
    @property
    def is_w(self) -> bool:
        return self.value == "W"
