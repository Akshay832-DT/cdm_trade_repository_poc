
from .base import FIXFieldBase
from .types import FIXInt

class AllocRejCode(FIXFieldBase):
    """FIX AllocRejCode field."""
    tag: str = "88"
    name: str = "AllocRejCode"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: UNKNOWN_ACCOUNT
    # 1: INCORRECT_QUANTITY
    # 2: INCORRECT_AVERAGEG_PRICE
    # 3: UNKNOWN_EXECUTING_BROKER_MNEMONIC
    # 4: COMMISSION_DIFFERENCE
    # 5: UNKNOWN_ORDER_ID
    # 6: UNKNOWN_LIST_ID
    # 7: OTHER_SEE_TEXT
    # 8: INCORRECT_ALLOCATED_QUANTITY
    # 9: CALCULATION_DIFFERENCE
    # 10: UNKNOWN_OR_STALE_EXEC_ID
    # 11: MISMATCHED_DATA
    # 12: UNKNOWN_CL_ORD_ID
    # 13: WAREHOUSE_REQUEST_REJECTED
