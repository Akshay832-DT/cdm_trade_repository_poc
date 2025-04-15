"""
FIX PosReqResult field (tag 728).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PosReqResultValues:
    """Enumerated values for PosReqResult."""
    VALUE_0 = "0"  # VALID_REQUEST
    VALUE_1 = "1"  # INVALID_OR_UNSUPPORTED_REQUEST
    VALUE_2 = "2"  # NO_POSITIONS_FOUND_THAT_MATCH_CRITERIA
    VALUE_3 = "3"  # NOT_AUTHORIZED_TO_REQUEST_POSITIONS
    VALUE_4 = "4"  # REQUEST_FOR_POSITION_NOT_SUPPORTED
    VALUE_99 = "99"  # OTHER

class PosReqResultField(FIXFieldBase):
    """"""
    tag: str = "728"
    name: str = "PosReqResult"
    type: str = "INT"
    value: Literal["0", "1", "2", "3", "4", "99"]

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
    def is_value_99(self) -> bool:
        return self.value == "99"
