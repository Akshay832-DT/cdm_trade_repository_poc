
from .base import FIXFieldBase
from .types import FIXChar

class ListExecInstType(FIXFieldBase):
    """FIX ListExecInstType field."""
    tag: str = "433"
    name: str = "ListExecInstType"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 1: IMMEDIATE
    # 2: WAIT_FOR_INSTRUCTION
    # 3: SELL_DRIVEN
    # 4: BUY_DRIVEN_CASH_TOP_UP
    # 5: BUY_DRIVEN_CASH_WITHDRAW
