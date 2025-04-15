"""
FIX OwnershipType field (tag 517).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OwnershipTypeValues:
    """Enumerated values for OwnershipType."""
    J = "J"  # JOINT_INVESTORS
    T = "T"  # TENANTS_IN_COMMON
    VALUE_2 = "2"  # JOINT_TRUSTEES

class OwnershipTypeField(FIXFieldBase):
    """"""
    tag: str = "517"
    name: str = "OwnershipType"
    type: str = "CHAR"
    value: Literal["J", "T", "2"]

    # Helper methods for enum values
    @property
    def is_j(self) -> bool:
        return self.value == "J"
    @property
    def is_t(self) -> bool:
        return self.value == "T"
    @property
    def is_value_2(self) -> bool:
        return self.value == "2"
