"""
FIX ResponseTransportType field (tag 725).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ResponseTransportTypeValues:
    """Enumerated values for ResponseTransportType."""
    VALUE_0 = "0"  # INBAND
    VALUE_1 = "1"  # OUT_OF_BAND

class ResponseTransportTypeField(FIXFieldBase):
    """"""
    tag: str = "725"
    name: str = "ResponseTransportType"
    type: str = "INT"
    value: Literal["0", "1"]

    # Helper methods for enum values
    @property
    def is_value_0(self) -> bool:
        return self.value == "0"
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
