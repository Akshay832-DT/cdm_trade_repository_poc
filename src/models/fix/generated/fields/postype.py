
from .base import FIXFieldBase
from .types import FIXString

class PosType(FIXFieldBase):
    """FIX PosType field."""
    tag: str = "703"
    name: str = "PosType"
    type: str = "STRING"
    value: FIXString

    # Enum values
    # TQ: TRANSACTION_QUANTITY
    # IAS: INTRA_SPREAD_QTY
    # IES: INTER_SPREAD_QTY
    # FIN: END_OF_DAY_QTY
    # SOD: START_OF_DAY_QTY
    # EX: OPTION_EXERCISE_QTY
    # AS: OPTION_ASSIGNMENT
    # TX: TRANSACTION_FROM_EXERCISE
    # TA: TRANSACTION_FROM_ASSIGNMENT
    # PIT: PIT_TRADE_QTY
    # TRF: TRANSFER_TRADE_QTY
    # ETR: ELECTRONIC_TRADE_QTY
    # ALC: ALLOCATION_TRADE_QTY
    # PA: ADJUSTMENT_QTY
    # ASF: AS_OF_TRADE_QTY
    # DLV: DELIVERY_QTY
    # TOT: TOTAL_TRANSACTION_QTY
    # XM: CROSS_MARGIN_QTY
    # SPL: INTEGRAL_SPLIT
