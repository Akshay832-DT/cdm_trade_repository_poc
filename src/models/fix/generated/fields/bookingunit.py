
from .base import FIXFieldBase
from .types import FIXChar

class BookingUnit(FIXFieldBase):
    """FIX BookingUnit field."""
    tag: str = "590"
    name: str = "BookingUnit"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 0: EACH_PARTIAL_EXECUTION_IS_A_BOOKABLE_UNIT
    # 1: AGGREGATE_PARTIAL_EXECUTIONS_ON_THIS_ORDER
    # 2: AGGREGATE_EXECUTIONS_FOR_THIS_SYMBOL
