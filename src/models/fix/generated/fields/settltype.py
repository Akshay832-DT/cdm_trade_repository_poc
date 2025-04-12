
from .base import FIXFieldBase
from .types import FIXChar

class SettlType(FIXFieldBase):
    """FIX SettlType field."""
    tag: str = "63"
    name: str = "SettlType"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 0: REGULAR
    # 1: CASH
    # 2: NEXT_DAY
    # 3: T_PLUS2
    # 4: T_PLUS3
    # 5: T_PLUS4
    # 6: FUTURE
    # 7: WHEN_AND_IF_ISSUED
    # 8: SELLERS_OPTION
    # 9: T_PLUS5
