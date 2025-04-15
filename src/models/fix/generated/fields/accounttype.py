"""
FIX AccountType field (tag 581).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AccountTypeValues:
    """Enumerated values for AccountType."""
    VALUE_1 = "1"  # CARRIED_CUSTOMER_SIDE
    VALUE_2 = "2"  # CARRIED_NON_CUSTOMER_SIDE
    VALUE_3 = "3"  # HOUSE_TRADER
    VALUE_4 = "4"  # FLOOR_TRADER
    VALUE_6 = "6"  # CARRIED_NON_CUSTOMER_SIDE_CROSS_MARGINED
    VALUE_7 = "7"  # HOUSE_TRADER_CROSS_MARGINED
    VALUE_8 = "8"  # JOINT_BACK_OFFICE_ACCOUNT

class AccountTypeField(FIXFieldBase):
    """"""
    tag: str = "581"
    name: str = "AccountType"
    type: str = "INT"
    value: Literal["1", "2", "3", "4", "6", "7", "8"]

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
    @property
    def is_value_4(self) -> bool:
        return self.value == "4"
    @property
    def is_value_6(self) -> bool:
        return self.value == "6"
    @property
    def is_value_7(self) -> bool:
        return self.value == "7"
    @property
    def is_value_8(self) -> bool:
        return self.value == "8"
