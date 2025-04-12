
from .base import FIXFieldBase
from .types import FIXString

class LocationID(FIXFieldBase):
    """FIX LocationID field."""
    tag: str = "283"
    name: str = "LocationID"
    type: str = "STRING"
    value: FIXString
