"""
FIX ForexReq field (tag 121).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ForexReqValues:
    """Enumerated values for ForexReq."""
    Y = "Y"  # YES
    N = "N"  # NO

class ForexReqField(FIXFieldBase):
    """"""
    tag: str = "121"
    name: str = "ForexReq"
    type: str = "BOOLEAN"
    value: Literal["Y", "N"]

    # Helper methods for enum values
    @property
    def is_y(self) -> bool:
        return self.value == "Y"
    @property
    def is_n(self) -> bool:
        return self.value == "N"
