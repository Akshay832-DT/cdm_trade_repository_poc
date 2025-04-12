
from .base import FIXFieldBase
from .types import FIXInt

class SettlDeliveryType(FIXFieldBase):
    """FIX SettlDeliveryType field."""
    tag: str = "172"
    name: str = "SettlDeliveryType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: VERSUS
    # 1: FREE
    # 2: TRI_PARTY
    # 3: HOLD_IN_CUSTODY
