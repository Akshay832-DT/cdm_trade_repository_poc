"""
FIX PartyRole field (tag 452).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PartyRoleValues:
    """Enumerated values for PartyRole."""
    VALUE_1 = "1"  # EXECUTING_FIRM
    VALUE_2 = "2"  # BROKER_OF_CREDIT
    VALUE_3 = "3"  # CLIENT_ID
    VALUE_4 = "4"  # CLEARING_FIRM
    VALUE_5 = "5"  # INVESTOR_ID
    VALUE_6 = "6"  # INTRODUCING_FIRM
    VALUE_7 = "7"  # ENTERING_FIRM
    VALUE_8 = "8"  # LOCATE
    VALUE_9 = "9"  # FUND_MANAGER_CLIENT_ID
    VALUE_10 = "10"  # SETTLEMENT_LOCATION
    VALUE_11 = "11"  # ORDER_ORIGINATION_TRADER
    VALUE_12 = "12"  # EXECUTING_TRADER
    VALUE_13 = "13"  # ORDER_ORIGINATION_FIRM
    VALUE_14 = "14"  # GIVEUP_CLEARING_FIRM
    VALUE_15 = "15"  # CORRESPONDANT_CLEARING_FIRM
    VALUE_16 = "16"  # EXECUTING_SYSTEM
    VALUE_17 = "17"  # CONTRA_FIRM
    VALUE_18 = "18"  # CONTRA_CLEARING_FIRM
    VALUE_19 = "19"  # SPONSORING_FIRM
    VALUE_20 = "20"  # UNDERLYING_CONTRA_FIRM
    VALUE_21 = "21"  # CLEARING_ORGANIZATION
    VALUE_22 = "22"  # EXCHANGE
    VALUE_24 = "24"  # CUSTOMER_ACCOUNT
    VALUE_25 = "25"  # CORRESPONDENT_CLEARING_ORGANIZATION
    VALUE_26 = "26"  # CORRESPONDENT_BROKER
    VALUE_27 = "27"  # BUYER
    VALUE_28 = "28"  # CUSTODIAN
    VALUE_29 = "29"  # INTERMEDIARY
    VALUE_30 = "30"  # AGENT
    VALUE_31 = "31"  # SUB_CUSTODIAN
    VALUE_32 = "32"  # BENEFICIARY
    VALUE_33 = "33"  # INTERESTED_PARTY
    VALUE_34 = "34"  # REGULATORY_BODY
    VALUE_35 = "35"  # LIQUIDITY_PROVIDER
    VALUE_36 = "36"  # ENTERING_TRADER
    VALUE_37 = "37"  # CONTRA_TRADER
    VALUE_38 = "38"  # POSITION_ACCOUNT

class PartyRoleField(FIXFieldBase):
    """"""
    tag: str = "452"
    name: str = "PartyRole"
    type: str = "INT"
    value: Literal["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38"]

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
    def is_value_24(self) -> bool:
        return self.value == "24"
    @property
    def is_value_25(self) -> bool:
        return self.value == "25"
    @property
    def is_value_26(self) -> bool:
        return self.value == "26"
    @property
    def is_value_27(self) -> bool:
        return self.value == "27"
    @property
    def is_value_28(self) -> bool:
        return self.value == "28"
    @property
    def is_value_29(self) -> bool:
        return self.value == "29"
    @property
    def is_value_30(self) -> bool:
        return self.value == "30"
    @property
    def is_value_31(self) -> bool:
        return self.value == "31"
    @property
    def is_value_32(self) -> bool:
        return self.value == "32"
    @property
    def is_value_33(self) -> bool:
        return self.value == "33"
    @property
    def is_value_34(self) -> bool:
        return self.value == "34"
    @property
    def is_value_35(self) -> bool:
        return self.value == "35"
    @property
    def is_value_36(self) -> bool:
        return self.value == "36"
    @property
    def is_value_37(self) -> bool:
        return self.value == "37"
    @property
    def is_value_38(self) -> bool:
        return self.value == "38"
