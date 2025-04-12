
from .base import FIXFieldBase
from .types import FIXInt

class ShortSaleReason(FIXFieldBase):
    """FIX ShortSaleReason field."""
    tag: str = "853"
    name: str = "ShortSaleReason"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: DEALER_SOLD_SHORT
    # 1: DEALER_SOLD_SHORT_EXEMPT
    # 2: SELLING_CUSTOMER_SOLD_SHORT
    # 3: SELLING_CUSTOMER_SOLD_SHORT_EXEMPT
    # 4: QUALIFIED_SERVICE_REPRESENTATIVE
    # 5: QSR_OR_AGU_CONTRA_SIDE_SOLD_SHORT_EXEMPT
