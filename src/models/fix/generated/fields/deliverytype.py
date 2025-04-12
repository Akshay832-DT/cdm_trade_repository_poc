
from .base import FIXFieldBase
from .types import FIXInt

class DeliveryType(FIXFieldBase):
    """FIX DeliveryType field."""
    tag: str = "919"
    name: str = "DeliveryType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: VERSUS_PAYMENT
    # 1: FREE
    # 2: TRI_PARTY
    # 3: HOLD_IN_CUSTODY
