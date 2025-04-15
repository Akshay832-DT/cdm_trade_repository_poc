"""
FIX SecurityRequestResult field (tag 560).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SecurityRequestResultValues:
    """Enumerated values for SecurityRequestResult."""
    VALUE_0 = "0"  # VALID_REQUEST
    VALUE_1 = "1"  # INVALID_OR_UNSUPPORTED_REQUEST
    VALUE_2 = "2"  # NO_INSTRUMENTS_FOUND
    VALUE_3 = "3"  # NOT_AUTHORIZED_TO_RETRIEVE_INSTRUMENT_DATA
    VALUE_4 = "4"  # INSTRUMENT_DATA_TEMPORARILY_UNAVAILABLE
    VALUE_5 = "5"  # REQUEST_FOR_INSTRUMENT_DATA_NOT_SUPPORTED

class SecurityRequestResultField(FIXFieldBase):
    """"""
    tag: str = "560"
    name: str = "SecurityRequestResult"
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
