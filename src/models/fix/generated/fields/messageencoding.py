"""
FIX MessageEncoding field (tag 347).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MessageEncodingValues:
    """Enumerated values for MessageEncoding."""
    ISO_2022_JP = "ISO-2022-JP"  # ISO2022_JP
    EUC_JP = "EUC-JP"  # EUCJP
    Shift_JIS = "Shift_JIS"  # SHIFT_JIS
    UTF_8 = "UTF-8"  # UTF8

class MessageEncodingField(FIXFieldBase):
    """"""
    tag: str = "347"
    name: str = "MessageEncoding"
    type: str = "STRING"
    value: Literal["ISO-2022-JP", "EUC-JP", "Shift_JIS", "UTF-8"]

    # Helper methods for enum values
    @property
    def is_iso_2022_jp(self) -> bool:
        return self.value == "ISO-2022-JP"
    @property
    def is_euc_jp(self) -> bool:
        return self.value == "EUC-JP"
    @property
    def is_shift_jis(self) -> bool:
        return self.value == "Shift_JIS"
    @property
    def is_utf_8(self) -> bool:
        return self.value == "UTF-8"
