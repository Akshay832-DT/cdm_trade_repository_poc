
from .base import FIXFieldBase
from .types import FIXString

class TransferReason(FIXFieldBase):
    """FIX TransferReason field."""
    tag: str = "830"
    name: str = "TransferReason"
    type: str = "STRING"
    value: FIXString
