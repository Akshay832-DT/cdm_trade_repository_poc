
from .base import FIXFieldBase
from .types import FIXString

class StandInstDbName(FIXFieldBase):
    """FIX StandInstDbName field."""
    tag: str = "170"
    name: str = "StandInstDbName"
    type: str = "STRING"
    value: FIXString
