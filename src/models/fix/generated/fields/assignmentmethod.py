"""
FIX AssignmentMethod field (tag 744).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AssignmentMethodValues:
    """Enumerated values for AssignmentMethod."""
    R = "R"  # RANDOM
    P = "P"  # PRO_RATA

class AssignmentMethodField(FIXFieldBase):
    """"""
    tag: str = "744"
    name: str = "AssignmentMethod"
    type: str = "CHAR"
    value: Literal["R", "P"]

    # Helper methods for enum values
    @property
    def is_r(self) -> bool:
        return self.value == "R"
    @property
    def is_p(self) -> bool:
        return self.value == "P"
