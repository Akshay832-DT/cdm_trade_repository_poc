"""
FIX ProgRptReqs field (tag 414).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ProgRptReqsValues:
    """Enumerated values for ProgRptReqs."""
    VALUE_1 = "1"  # BUY_SIDE_REQUESTS
    VALUE_2 = "2"  # SELL_SIDE_SENDS
    VALUE_3 = "3"  # REAL_TIME_EXECUTION_REPORTS

class ProgRptReqsField(FIXFieldBase):
    """"""
    tag: str = "414"
    name: str = "ProgRptReqs"
    type: str = "INT"
    value: Literal["1", "2", "3"]

    # Helper methods for enum values
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
    @property
    def is_value_2(self) -> bool:
        return self.value == "2"
    @property
    def is_value_3(self) -> bool:
        return self.value == "3"
