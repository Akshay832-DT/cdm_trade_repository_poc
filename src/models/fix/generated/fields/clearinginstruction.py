
from .base import FIXFieldBase
from .types import FIXInt

class ClearingInstruction(FIXFieldBase):
    """FIX ClearingInstruction field."""
    tag: str = "577"
    name: str = "ClearingInstruction"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: PROCESS_NORMALLY
    # 1: EXCLUDE_FROM_ALL_NETTING
    # 2: BILATERAL_NETTING_ONLY
    # 3: EX_CLEARING
    # 4: SPECIAL_TRADE
    # 5: MULTILATERAL_NETTING
    # 6: CLEAR_AGAINST_CENTRAL_COUNTERPARTY
    # 7: EXCLUDE_FROM_CENTRAL_COUNTERPARTY
    # 8: MANUAL_MODE
    # 9: AUTOMATIC_POSTING_MODE
    # 10: AUTOMATIC_GIVE_UP_MODE
    # 11: QUALIFIED_SERVICE_REPRESENTATIVE_QSR
    # 12: CUSTOMER_TRADE
    # 13: SELF_CLEARING
