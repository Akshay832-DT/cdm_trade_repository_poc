
from .base import FIXFieldBase
from .types import FIXChar

class EmailType(FIXFieldBase):
    """FIX EmailType field."""
    tag: str = "94"
    name: str = "EmailType"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 0: NEW
    # 1: REPLY
    # 2: ADMIN_REPLY
