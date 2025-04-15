"""
FIX PosMaintResult field (tag 723).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PosMaintResultValues:
    """Enumerated values for PosMaintResult."""
    VALUE_0 = "0"  # SUCCESSFUL_COMPLETION
    VALUE_1 = "1"  # REJECTED
    VALUE_99 = "99"  # OTHER

class PosMaintResultField(FIXFieldBase):
    """"""
    tag: str = "723"
    name: str = "PosMaintResult"
    type: str = "INT"
    value: Literal["0", "1", "99"]

    # Helper methods for enum values
    @property
    def is_value_0(self) -> bool:
        return self.value == "0"
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
    @property
    def is_value_99(self) -> bool:
        return self.value == "99"
