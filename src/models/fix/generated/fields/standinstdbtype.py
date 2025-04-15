"""
FIX StandInstDbType field (tag 169).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class StandInstDbTypeValues:
    """Enumerated values for StandInstDbType."""
    VALUE_0 = "0"  # OTHER
    VALUE_1 = "1"  # DTCSID
    VALUE_2 = "2"  # THOMSON_ALERT
    VALUE_3 = "3"  # A_GLOBAL_CUSTODIAN
    VALUE_4 = "4"  # ACCOUNT_NET

class StandInstDbTypeField(FIXFieldBase):
    """"""
    tag: str = "169"
    name: str = "StandInstDbType"
    type: str = "INT"
    value: Literal["0", "1", "2", "3", "4"]

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
    @property
    def is_value_4(self) -> bool:
        return self.value == "4"
