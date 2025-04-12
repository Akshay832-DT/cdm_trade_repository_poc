
from .base import FIXFieldBase
from .types import FIXMultipleValueString

class OpenCloseSettlFlag(FIXFieldBase):
    """FIX OpenCloseSettlFlag field."""
    tag: str = "286"
    name: str = "OpenCloseSettlFlag"
    type: str = "MULTIPLEVALUESTRING"
    value: FIXMultipleValueString

    # Enum values
    # 0: DAILY_OPEN
    # 1: SESSION_OPEN
    # 2: DELIVERY_SETTLEMENT_ENTRY
    # 3: EXPECTED_ENTRY
    # 4: ENTRY_FROM_PREVIOUS_BUSINESS_DAY
    # 5: THEORETICAL_PRICE_VALUE
