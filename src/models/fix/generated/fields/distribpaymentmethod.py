
from .base import FIXFieldBase
from .types import FIXInt

class DistribPaymentMethod(FIXFieldBase):
    """FIX DistribPaymentMethod field."""
    tag: str = "477"
    name: str = "DistribPaymentMethod"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: CREST
    # 2: NSCC
    # 3: EUROCLEAR
    # 4: CLEARSTREAM
    # 5: CHEQUE
    # 6: TELEGRAPHIC_TRANSFER
    # 7: FED_WIRE
    # 8: DIRECT_CREDIT
    # 9: ACH_CREDIT
    # 10: BPAY
    # 11: HIGH_VALUE_CLEARING_SYSTEM_HVACS
    # 12: REINVEST_IN_FUND
