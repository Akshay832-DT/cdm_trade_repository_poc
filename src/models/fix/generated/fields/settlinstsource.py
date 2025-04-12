
from .base import FIXFieldBase
from .types import FIXChar

class SettlInstSource(FIXFieldBase):
    """FIX SettlInstSource field."""
    tag: str = "165"
    name: str = "SettlInstSource"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 1: BROKER_CREDIT
    # 2: INSTITUTION
    # 3: INVESTOR
