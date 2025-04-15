"""
FIX CPProgram field (tag 875).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CPProgramValues:
    """Enumerated values for CPProgram."""
    VALUE_1 = "1"  # PROGRAM3A3
    VALUE_2 = "2"  # PROGRAM42
    VALUE_99 = "99"  # OTHER

class CPProgramField(FIXFieldBase):
    """"""
    tag: str = "875"
    name: str = "CPProgram"
    type: str = "INT"
    value: Literal["1", "2", "99"]

    # Helper methods for enum values
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
    @property
    def is_value_2(self) -> bool:
        return self.value == "2"
    @property
    def is_value_99(self) -> bool:
        return self.value == "99"
