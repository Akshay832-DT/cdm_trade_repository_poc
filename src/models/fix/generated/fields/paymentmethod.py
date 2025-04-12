
from .base import FIXFieldBase
from .types import FIXInt

class PaymentMethod(FIXFieldBase):
    """FIX PaymentMethod field."""
    tag: str = "492"
    name: str = "PaymentMethod"
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
    # 8: DEBIT_CARD
    # 9: DIRECT_DEBIT
    # 10: DIRECT_CREDIT
    # 11: CREDIT_CARD
    # 12: ACH_DEBIT
    # 13: ACH_CREDIT
    # 14: BPAY
    # 15: HIGH_VALUE_CLEARING_SYSTEM
