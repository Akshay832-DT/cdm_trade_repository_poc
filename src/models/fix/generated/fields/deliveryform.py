"""
FIX DeliveryForm field (tag 668).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class DeliveryFormValues:
    """Enumerated values for DeliveryForm."""
    VALUE_1 = "1"  # BOOK_ENTRY
    VALUE_2 = "2"  # BEARER

class DeliveryFormField(FIXFieldBase):
    """"""
    tag: str = "668"
    name: str = "DeliveryForm"
    type: str = "INT"
    value: Literal["1", "2"]

    # Helper methods for enum values
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
    @property
    def is_value_2(self) -> bool:
        return self.value == "2"
