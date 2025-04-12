
from .base import FIXFieldBase
from .types import FIXChar

class MatchStatus(FIXFieldBase):
    """FIX MatchStatus field."""
    tag: str = "573"
    name: str = "MatchStatus"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 0: COMPARED
    # 1: UNCOMPARED
    # 2: ADVISORY_OR_ALERT
