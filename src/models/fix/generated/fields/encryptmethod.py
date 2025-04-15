"""
FIX EncryptMethod field (tag 98).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EncryptMethodValues:
    """Enumerated values for EncryptMethod."""
    VALUE_0 = "0"  # NONE
    VALUE_1 = "1"  # PKCS
    VALUE_2 = "2"  # DES
    VALUE_3 = "3"  # PKCSDES
    VALUE_4 = "4"  # PGPDES
    VALUE_5 = "5"  # PGPDESMD5
    VALUE_6 = "6"  # PEM

class EncryptMethodField(FIXFieldBase):
    """"""
    tag: str = "98"
    name: str = "EncryptMethod"
    type: str = "INT"
    value: Literal["0", "1", "2", "3", "4", "5", "6"]

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
