
from .base import FIXFieldBase
from .types import FIXChar

class CommType(FIXFieldBase):
    """FIX CommType field."""
    tag: str = "13"
    name: str = "CommType"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 1: PER_UNIT
    # 2: PERCENT
    # 3: ABSOLUTE
    # 4: PERCENTAGE_WAIVED_CASH_DISCOUNT
    # 5: PERCENTAGE_WAIVED_ENHANCED_UNITS
    # 6: POINTS_PER_BOND_OR_CONTRACT
