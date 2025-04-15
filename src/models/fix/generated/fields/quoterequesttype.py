"""
FIX QuoteRequestType field (tag 303).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class QuoteRequestTypeValues:
    """Enumerated values for QuoteRequestType."""
    VALUE_1 = "1"  # MANUAL
    VALUE_2 = "2"  # AUTOMATIC

class QuoteRequestTypeField(FIXFieldBase):
    """"""
    tag: str = "303"
    name: str = "QuoteRequestType"
    type: str = "INT"
    value: Literal["1", "2"]

    # Helper methods for enum values
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
    @property
    def is_value_2(self) -> bool:
        return self.value == "2"
