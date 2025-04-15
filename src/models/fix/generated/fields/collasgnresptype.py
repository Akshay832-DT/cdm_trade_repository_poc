"""
FIX CollAsgnRespType field (tag 905).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CollAsgnRespTypeValues:
    """Enumerated values for CollAsgnRespType."""
    VALUE_0 = "0"  # RECEIVED
    VALUE_1 = "1"  # ACCEPTED
    VALUE_2 = "2"  # DECLINED
    VALUE_3 = "3"  # REJECTED

class CollAsgnRespTypeField(FIXFieldBase):
    """"""
    tag: str = "905"
    name: str = "CollAsgnRespType"
    type: str = "INT"
    value: Literal["0", "1", "2", "3"]

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
    @property
    def is_value_3(self) -> bool:
        return self.value == "3"
