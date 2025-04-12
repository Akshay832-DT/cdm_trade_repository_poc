
from .base import FIXFieldBase
from .types import FIXChar

class HaltReasonChar(FIXFieldBase):
    """FIX HaltReasonChar field."""
    tag: str = "327"
    name: str = "HaltReasonChar"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # I: ORDER_IMBALANCE
    # X: EQUIPMENT_CHANGEOVER
    # P: NEWS_PENDING
    # D: NEWS_DISSEMINATION
    # E: ORDER_INFLUX
    # M: ADDITIONAL_INFORMATION
