"""
FIX SecurityResponseType field (tag 323).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SecurityResponseTypeValues:
    """Enumerated values for SecurityResponseType."""
    VALUE_1 = "1"  # ACCEPT_AS_IS
    VALUE_2 = "2"  # ACCEPT_WITH_REVISIONS
    VALUE_5 = "5"  # REJECT_SECURITY_PROPOSAL
    VALUE_6 = "6"  # CANNOT_MATCH_SELECTION_CRITERIA

class SecurityResponseTypeField(FIXFieldBase):
    """"""
    tag: str = "323"
    name: str = "SecurityResponseType"
    type: str = "INT"
    value: Literal["1", "2", "5", "6"]

    # Helper methods for enum values
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
    @property
    def is_value_2(self) -> bool:
        return self.value == "2"
    @property
    def is_value_5(self) -> bool:
        return self.value == "5"
    @property
    def is_value_6(self) -> bool:
        return self.value == "6"
