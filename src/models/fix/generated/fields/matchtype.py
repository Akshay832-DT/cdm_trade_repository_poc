"""
FIX MatchType field (tag 574).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MatchTypeValues:
    """Enumerated values for MatchType."""
    A1 = "A1"  # EXACT_MATCH_PLUS4_BADGES_EXEC_TIME
    A2 = "A2"  # EXACT_MATCH_PLUS4_BADGES
    A3 = "A3"  # EXACT_MATCH_PLUS2_BADGES_EXEC_TIME
    A4 = "A4"  # EXACT_MATCH_PLUS2_BADGES
    A5 = "A5"  # EXACT_MATCH_PLUS_EXEC_TIME
    AQ = "AQ"  # STAMPED_ADVISORIES_OR_SPECIALIST_ACCEPTS
    S1 = "S1"  # A1_EXACT_MATCH_SUMMARIZED_QUANTITY
    S2 = "S2"  # A2_EXACT_MATCH_SUMMARIZED_QUANTITY
    S3 = "S3"  # A3_EXACT_MATCH_SUMMARIZED_QUANTITY
    S4 = "S4"  # A4_EXACT_MATCH_SUMMARIZED_QUANTITY
    S5 = "S5"  # A5_EXACT_MATCH_SUMMARIZED_QUANTITY
    M1 = "M1"  # EXACT_MATCH_MINUS_BADGES_TIMES
    M2 = "M2"  # SUMMARIZED_MATCH_MINUS_BADGES_TIMES
    MT = "MT"  # OCS_LOCKED_IN
    M3 = "M3"  # ACT_ACCEPTED_TRADE
    M4 = "M4"  # ACT_DEFAULT_TRADE
    M5 = "M5"  # ACT_DEFAULT_AFTER_M2
    M6 = "M6"  # ACTM6_MATCH

class MatchTypeField(FIXFieldBase):
    """"""
    tag: str = "574"
    name: str = "MatchType"
    type: str = "STRING"
    value: Literal["A1", "A2", "A3", "A4", "A5", "AQ", "S1", "S2", "S3", "S4", "S5", "M1", "M2", "MT", "M3", "M4", "M5", "M6"]

    # Helper methods for enum values
    @property
    def is_a1(self) -> bool:
        return self.value == "A1"
    @property
    def is_a2(self) -> bool:
        return self.value == "A2"
    @property
    def is_a3(self) -> bool:
        return self.value == "A3"
    @property
    def is_a4(self) -> bool:
        return self.value == "A4"
    @property
    def is_a5(self) -> bool:
        return self.value == "A5"
    @property
    def is_aq(self) -> bool:
        return self.value == "AQ"
    @property
    def is_s1(self) -> bool:
        return self.value == "S1"
    @property
    def is_s2(self) -> bool:
        return self.value == "S2"
    @property
    def is_s3(self) -> bool:
        return self.value == "S3"
    @property
    def is_s4(self) -> bool:
        return self.value == "S4"
    @property
    def is_s5(self) -> bool:
        return self.value == "S5"
    @property
    def is_m1(self) -> bool:
        return self.value == "M1"
    @property
    def is_m2(self) -> bool:
        return self.value == "M2"
    @property
    def is_mt(self) -> bool:
        return self.value == "MT"
    @property
    def is_m3(self) -> bool:
        return self.value == "M3"
    @property
    def is_m4(self) -> bool:
        return self.value == "M4"
    @property
    def is_m5(self) -> bool:
        return self.value == "M5"
    @property
    def is_m6(self) -> bool:
        return self.value == "M6"
