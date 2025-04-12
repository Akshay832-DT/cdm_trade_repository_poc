
from .base import FIXFieldBase
from .types import FIXInt

class StandInstDbType(FIXFieldBase):
    """FIX StandInstDbType field."""
    tag: str = "169"
    name: str = "StandInstDbType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: OTHER
    # 1: DTCSID
    # 2: THOMSON_ALERT
    # 3: A_GLOBAL_CUSTODIAN
    # 4: ACCOUNT_NET
