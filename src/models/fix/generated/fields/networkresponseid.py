
from .base import FIXFieldBase
from .types import FIXString

class NetworkResponseID(FIXFieldBase):
    """FIX NetworkResponseID field."""
    tag: str = "932"
    name: str = "NetworkResponseID"
    type: str = "STRING"
    value: FIXString
