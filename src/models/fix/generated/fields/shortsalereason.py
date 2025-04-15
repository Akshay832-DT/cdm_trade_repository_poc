"""
FIX ShortSaleReason field (tag 853).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ShortSaleReasonValues:
    """Enumerated values for ShortSaleReason."""
    VALUE_0 = "0"  # DEALER_SOLD_SHORT
    VALUE_1 = "1"  # DEALER_SOLD_SHORT_EXEMPT
    VALUE_2 = "2"  # SELLING_CUSTOMER_SOLD_SHORT
    VALUE_3 = "3"  # SELLING_CUSTOMER_SOLD_SHORT_EXEMPT
    VALUE_4 = "4"  # QUALIFIED_SERVICE_REPRESENTATIVE
    VALUE_5 = "5"  # QSR_OR_AGU_CONTRA_SIDE_SOLD_SHORT_EXEMPT

class ShortSaleReasonField(FIXFieldBase):
    """"""
    tag: str = "853"
    name: str = "ShortSaleReason"
    type: str = "INT"
    value: Literal["0", "1", "2", "3", "4", "5"]

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
    @property
    def is_value_5(self) -> bool:
        return self.value == "5"
