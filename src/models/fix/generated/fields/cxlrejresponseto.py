
from .base import FIXFieldBase
from .types import FIXChar

class CxlRejResponseTo(FIXFieldBase):
    """FIX CxlRejResponseTo field."""
    tag: str = "434"
    name: str = "CxlRejResponseTo"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 1: ORDER_CANCEL_REQUEST
    # 2: ORDER_CANCEL
