"""
FIX QuoteResponseLevel field (tag 301).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class QuoteResponseLevelValues:
    """Enumerated values for QuoteResponseLevel."""
    VALUE_0 = "0"  # NO_ACKNOWLEDGEMENT
    VALUE_1 = "1"  # ACKNOWLEDGE_ONLY_NEGATIVE_OR_ERRONEOUS_QUOTES
    VALUE_2 = "2"  # ACKNOWLEDGE_EACH_QUOTE_MESSAGE

class QuoteResponseLevelField(FIXFieldBase):
    """"""
    tag: str = "301"
    name: str = "QuoteResponseLevel"
    type: str = "INT"
    value: Literal["0", "1", "2"]

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
