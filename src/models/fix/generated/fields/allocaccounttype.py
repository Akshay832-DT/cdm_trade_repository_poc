
from .base import FIXFieldBase
from .types import FIXInt

class AllocAccountType(FIXFieldBase):
    """FIX AllocAccountType field."""
    tag: str = "798"
    name: str = "AllocAccountType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: CARRIED_CUSTOMER_SIDE
    # 2: CARRIED_NON_CUSTOMER_SIDE
    # 3: HOUSE_TRADER
    # 4: FLOOR_TRADER
    # 6: CARRIED_NON_CUSTOMER_SIDE_CROSS_MARGINED
    # 7: HOUSE_TRADER_CROSS_MARGINED
    # 8: JOINT_BACK_OFFICE_ACCOUNT
