"""
FIX MsgDirection field (tag 385).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MsgDirectionValues:
    """Enumerated values for MsgDirection."""
    S = "S"  # SEND
    R = "R"  # RECEIVE

class MsgDirectionField(FIXFieldBase):
    """"""
    tag: str = "385"
    name: str = "MsgDirection"
    type: str = "CHAR"
    value: Literal["S", "R"]

    # Helper methods for enum values
    @property
    def is_s(self) -> bool:
        return self.value == "S"
    @property
    def is_r(self) -> bool:
        return self.value == "R"
