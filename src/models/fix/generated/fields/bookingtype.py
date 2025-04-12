
from .base import FIXFieldBase
from .types import FIXInt

class BookingType(FIXFieldBase):
    """FIX BookingType field."""
    tag: str = "775"
    name: str = "BookingType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: REGULAR_BOOKING
    # 1: CFD
    # 2: TOTAL_RETURN_SWAP
