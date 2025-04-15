"""
FIX PartyIDSource field (tag 447).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PartyIDSourceValues:
    """Enumerated values for PartyIDSource."""
    B = "B"  # BIC
    C = "C"  # GENERAL_IDENTIFIER
    D = "D"  # PROPRIETARY
    E = "E"  # ISO_COUNTRY_CODE
    F = "F"  # SETTLEMENT_ENTITY_LOCATION
    G = "G"  # MIC
    H = "H"  # CSD_PARTICIPANT
    VALUE_1 = "1"  # KOREAN_INVESTOR_ID
    VALUE_2 = "2"  # TAIWANESE_FOREIGN_INVESTOR_ID
    VALUE_3 = "3"  # TAIWANESE_TRADING_ACCT
    VALUE_4 = "4"  # MALAYSIAN_CENTRAL_DEPOSITORY
    VALUE_5 = "5"  # CHINESE_INVESTOR_ID
    VALUE_6 = "6"  # UK_NATIONAL_INSURANCE_OR_PENSION_NUMBER
    VALUE_7 = "7"  # US_SOCIAL_SECURITY_NUMBER
    VALUE_8 = "8"  # US_EMPLOYER_OR_TAX_ID_NUMBER
    VALUE_9 = "9"  # AUSTRALIAN_BUSINESS_NUMBER
    A = "A"  # AUSTRALIAN_TAX_FILE_NUMBER
    I = "I"  # ISITC_ACRONYM

class PartyIDSourceField(FIXFieldBase):
    """"""
    tag: str = "447"
    name: str = "PartyIDSource"
    type: str = "CHAR"
    value: Literal["B", "C", "D", "E", "F", "G", "H", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "I"]

    # Helper methods for enum values
    @property
    def is_b(self) -> bool:
        return self.value == "B"
    @property
    def is_c(self) -> bool:
        return self.value == "C"
    @property
    def is_d(self) -> bool:
        return self.value == "D"
    @property
    def is_e(self) -> bool:
        return self.value == "E"
    @property
    def is_f(self) -> bool:
        return self.value == "F"
    @property
    def is_g(self) -> bool:
        return self.value == "G"
    @property
    def is_h(self) -> bool:
        return self.value == "H"
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
    def is_a(self) -> bool:
        return self.value == "A"
    @property
    def is_i(self) -> bool:
        return self.value == "I"
