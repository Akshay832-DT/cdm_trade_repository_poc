"""
FIX PartySubIDType field (tag 803).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PartySubIDTypeValues:
    """Enumerated values for PartySubIDType."""
    VALUE_1 = "1"  # FIRM
    VALUE_2 = "2"  # PERSON
    VALUE_3 = "3"  # SYSTEM
    VALUE_4 = "4"  # APPLICATION
    VALUE_5 = "5"  # FULL_LEGAL_NAME_OF_FIRM
    VALUE_6 = "6"  # POSTAL_ADDRESS
    VALUE_7 = "7"  # PHONE_NUMBER
    VALUE_8 = "8"  # EMAIL_ADDRESS
    VALUE_9 = "9"  # CONTACT_NAME
    VALUE_10 = "10"  # SECURITIES_ACCOUNT_NUMBER
    VALUE_11 = "11"  # REGISTRATION_NUMBER
    VALUE_12 = "12"  # REGISTERED_ADDRESS_FOR_CONFIRMATION
    VALUE_13 = "13"  # REGULATORY_STATUS
    VALUE_14 = "14"  # REGISTRATION_NAME
    VALUE_15 = "15"  # CASH_ACCOUNT_NUMBER
    VALUE_16 = "16"  # BIC
    VALUE_17 = "17"  # CSD_PARTICIPANT_MEMBER_CODE
    VALUE_18 = "18"  # REGISTERED_ADDRESS
    VALUE_19 = "19"  # FUND_ACCOUNT_NAME
    VALUE_20 = "20"  # TELEX_NUMBER
    VALUE_21 = "21"  # FAX_NUMBER
    VALUE_22 = "22"  # SECURITIES_ACCOUNT_NAME
    VALUE_23 = "23"  # CASH_ACCOUNT_NAME
    VALUE_24 = "24"  # DEPARTMENT
    VALUE_25 = "25"  # LOCATION_DESK
    VALUE_26 = "26"  # POSITION_ACCOUNT_TYPE

class PartySubIDTypeField(FIXFieldBase):
    """"""
    tag: str = "803"
    name: str = "PartySubIDType"
    type: str = "INT"
    value: Literal["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26"]

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
    def is_value_18(self) -> bool:
        return self.value == "18"
    @property
    def is_value_19(self) -> bool:
        return self.value == "19"
    @property
    def is_value_20(self) -> bool:
        return self.value == "20"
    @property
    def is_value_21(self) -> bool:
        return self.value == "21"
    @property
    def is_value_22(self) -> bool:
        return self.value == "22"
    @property
    def is_value_23(self) -> bool:
        return self.value == "23"
    @property
    def is_value_24(self) -> bool:
        return self.value == "24"
    @property
    def is_value_25(self) -> bool:
        return self.value == "25"
    @property
    def is_value_26(self) -> bool:
        return self.value == "26"
