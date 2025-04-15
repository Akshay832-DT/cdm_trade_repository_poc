"""
FIX TaxAdvantageType field (tag 495).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TaxAdvantageTypeValues:
    """Enumerated values for TaxAdvantageType."""
    VALUE_0 = "0"  # NONE
    VALUE_1 = "1"  # MAXI_ISA
    VALUE_2 = "2"  # TESSA
    VALUE_3 = "3"  # MINI_CASH_ISA
    VALUE_4 = "4"  # MINI_STOCKS_AND_SHARES_ISA
    VALUE_5 = "5"  # MINI_INSURANCE_ISA
    VALUE_6 = "6"  # CURRENT_YEAR_PAYMENT
    VALUE_7 = "7"  # PRIOR_YEAR_PAYMENT
    VALUE_8 = "8"  # ASSET_TRANSFER
    VALUE_9 = "9"  # EMPLOYEE_PRIOR_YEAR
    VALUE_10 = "10"  # EMPLOYEE_CURRENT_YEAR
    VALUE_11 = "11"  # EMPLOYER_PRIOR_YEAR
    VALUE_12 = "12"  # EMPLOYER_CURRENT_YEAR
    VALUE_13 = "13"  # NON_FUND_PROTOTYPE_IRA
    VALUE_14 = "14"  # NON_FUND_QUALIFIED_PLAN
    VALUE_15 = "15"  # DEFINED_CONTRIBUTION_PLAN
    VALUE_16 = "16"  # IRA
    VALUE_17 = "17"  # IRA_ROLLOVER
    VALUE_18 = "18"  # KEOGH
    VALUE_19 = "19"  # PROFIT_SHARING_PLAN
    VALUE_20 = "20"  # US401_K
    VALUE_21 = "21"  # SELF_DIRECTED_IRA
    VALUE_22 = "22"  # US403B
    VALUE_23 = "23"  # US457
    VALUE_24 = "24"  # ROTH_IRA_PROTOTYPE
    VALUE_25 = "25"  # ROTH_IRA_NON_PROTOTYPE
    VALUE_26 = "26"  # ROTH_CONVERSION_IRA_PROTOTYPE
    VALUE_27 = "27"  # ROTH_CONVERSION_IRA_NON_PROTOTYPE
    VALUE_28 = "28"  # EDUCATION_IRA_PROTOTYPE
    VALUE_29 = "29"  # EDUCATION_IRA_NON_PROTOTYPE

class TaxAdvantageTypeField(FIXFieldBase):
    """"""
    tag: str = "495"
    name: str = "TaxAdvantageType"
    type: str = "INT"
    value: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29"]

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
    @property
    def is_value_27(self) -> bool:
        return self.value == "27"
    @property
    def is_value_28(self) -> bool:
        return self.value == "28"
    @property
    def is_value_29(self) -> bool:
        return self.value == "29"
