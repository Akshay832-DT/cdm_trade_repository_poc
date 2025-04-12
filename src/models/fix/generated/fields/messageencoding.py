
from .base import FIXFieldBase
from .types import FIXString

class MessageEncoding(FIXFieldBase):
    """FIX MessageEncoding field."""
    tag: str = "347"
    name: str = "MessageEncoding"
    type: str = "STRING"
    value: FIXString

    # Enum values
    # ISO-2022-JP: ISO2022_JP
    # EUC-JP: EUCJP
    # Shift_JIS: SHIFT_JIS
    # UTF-8: UTF8
