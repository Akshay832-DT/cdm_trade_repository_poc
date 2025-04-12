
from .base import FIXFieldBase
from .types import FIXString

class BookingRefID(FIXFieldBase):
    """FIX BookingRefID field."""
    tag: str = "466"
    name: str = "BookingRefID"
    type: str = "STRING"
    value: FIXString
