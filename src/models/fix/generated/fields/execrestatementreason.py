
from .base import FIXFieldBase
from .types import FIXInt

class ExecRestatementReason(FIXFieldBase):
    """FIX ExecRestatementReason field."""
    tag: str = "378"
    name: str = "ExecRestatementReason"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: GT_CORPORATE_ACTION
    # 1: GT_RENEWAL
    # 2: VERBAL_CHANGE
    # 3: REPRICING_OF_ORDER
    # 4: BROKER_OPTION
    # 5: PARTIAL_DECLINE_OF_ORDER_QTY
    # 6: CANCEL_ON_TRADING_HALT
    # 7: CANCEL_ON_SYSTEM_FAILURE
    # 8: MARKET
    # 9: CANCELED
    # 10: WAREHOUSE_RECAP
    # 99: OTHER
