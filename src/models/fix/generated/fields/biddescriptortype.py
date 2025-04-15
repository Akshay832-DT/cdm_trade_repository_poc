"""
FIX BidDescriptorType field (tag 399).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class BidDescriptorTypeValues:
    """Enumerated values for BidDescriptorType."""
    VALUE_1 = "1"  # SECTOR
    VALUE_2 = "2"  # COUNTRY
    VALUE_3 = "3"  # INDEX

class BidDescriptorTypeField(FIXFieldBase):
    """"""
    tag: str = "399"
    name: str = "BidDescriptorType"
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
