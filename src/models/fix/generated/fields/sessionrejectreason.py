"""
FIX SessionRejectReason field (tag 373).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SessionRejectReasonValues:
    """Enumerated values for SessionRejectReason."""
    VALUE_0 = "0"  # INVALID_TAG_NUMBER
    VALUE_1 = "1"  # REQUIRED_TAG_MISSING
    VALUE_2 = "2"  # TAG_NOT_DEFINED_FOR_THIS_MESSAGE_TYPE
    VALUE_3 = "3"  # UNDEFINED_TAG
    VALUE_4 = "4"  # TAG_SPECIFIED_WITHOUT_A_VALUE
    VALUE_5 = "5"  # VALUE_IS_INCORRECT
    VALUE_6 = "6"  # INCORRECT_DATA_FORMAT_FOR_VALUE
    VALUE_7 = "7"  # DECRYPTION_PROBLEM
    VALUE_8 = "8"  # SIGNATURE_PROBLEM
    VALUE_9 = "9"  # COMP_ID_PROBLEM
    VALUE_10 = "10"  # SENDING_TIME_ACCURACY_PROBLEM
    VALUE_11 = "11"  # INVALID_MSG_TYPE
    VALUE_12 = "12"  # XML_VALIDATION_ERROR
    VALUE_13 = "13"  # TAG_APPEARS_MORE_THAN_ONCE
    VALUE_14 = "14"  # TAG_SPECIFIED_OUT_OF_REQUIRED_ORDER
    VALUE_15 = "15"  # REPEATING_GROUP_FIELDS_OUT_OF_ORDER
    VALUE_16 = "16"  # INCORRECT_NUM_IN_GROUP_COUNT_FOR_REPEATING_GROUP
    VALUE_17 = "17"  # NON
    VALUE_99 = "99"  # OTHER

class SessionRejectReasonField(FIXFieldBase):
    """"""
    tag: str = "373"
    name: str = "SessionRejectReason"
    type: str = "INT"
    value: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "99"]

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
    @property
    def is_value_6(self) -> bool:
        return self.value == "6"
    @property
    def is_value_7(self) -> bool:
        return self.value == "7"
    @property
    def is_value_8(self) -> bool:
        return self.value == "8"
    @property
    def is_value_9(self) -> bool:
        return self.value == "9"
    @property
    def is_value_10(self) -> bool:
        return self.value == "10"
    @property
    def is_value_11(self) -> bool:
        return self.value == "11"
    @property
    def is_value_12(self) -> bool:
        return self.value == "12"
    @property
    def is_value_13(self) -> bool:
        return self.value == "13"
    @property
    def is_value_14(self) -> bool:
        return self.value == "14"
    @property
    def is_value_15(self) -> bool:
        return self.value == "15"
    @property
    def is_value_16(self) -> bool:
        return self.value == "16"
    @property
    def is_value_17(self) -> bool:
        return self.value == "17"
    @property
    def is_value_99(self) -> bool:
        return self.value == "99"
