"""
FIX NetworkStatusResponseType field (tag 937).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NetworkStatusResponseTypeValues:
    """Enumerated values for NetworkStatusResponseType."""
    VALUE_1 = "1"  # FULL
    VALUE_2 = "2"  # INCREMENTAL_UPDATE

class NetworkStatusResponseTypeField(FIXFieldBase):
    """"""
    tag: str = "937"
    name: str = "NetworkStatusResponseType"
    type: str = "INT"
    value: Literal["1", "2"]

    # Helper methods for enum values
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
    @property
    def is_value_2(self) -> bool:
        return self.value == "2"
