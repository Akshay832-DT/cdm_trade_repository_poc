
from .base import FIXFieldBase
from .types import FIXString

class ClearingFeeIndicator(FIXFieldBase):
    """FIX ClearingFeeIndicator field."""
    tag: str = "635"
    name: str = "ClearingFeeIndicator"
    type: str = "STRING"
    value: FIXString

    # Enum values
    # B: CBOE_MEMBER
    # C: NON_MEMBER_AND_CUSTOMER
    # E: EQUITY_MEMBER_AND_CLEARING_MEMBER
    # F: FULL_AND_ASSOCIATE_MEMBER
    # H: FIRMS106_H_AND106_J
    # I: GIM
    # L: LESSEE106_F_EMPLOYEES
    # M: ALL_OTHER_OWNERSHIP_TYPES
    # 1: FIRST_YEAR_DELEGATE
    # 2: SECOND_YEAR_DELEGATE
    # 3: THIRD_YEAR_DELEGATE
    # 4: FOURTH_YEAR_DELEGATE
    # 5: FIFTH_YEAR_DELEGATE
    # 9: SIXTH_YEAR_DELEGATE
