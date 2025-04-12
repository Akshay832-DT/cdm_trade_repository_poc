
from .base import FIXFieldBase
from .types import FIXInt

class CxlRejReason(FIXFieldBase):
    """FIX CxlRejReason field."""
    tag: str = "102"
    name: str = "CxlRejReason"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: TOO_LATE_TO_CANCEL
    # 1: UNKNOWN_ORDER
    # 2: BROKER_CREDIT
    # 3: ORDER_ALREADY_IN_PENDING_STATUS
    # 4: UNABLE_TO_PROCESS_ORDER_MASS_CANCEL_REQUEST
    # 5: ORIG_ORD_MOD_TIME
    # 6: DUPLICATE_CL_ORD_ID
    # 99: OTHER
