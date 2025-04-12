
from .base import FIXFieldBase
from .types import FIXString

class AffectedOrderID(FIXFieldBase):
    """FIX AffectedOrderID field."""
    tag: str = "535"
    name: str = "AffectedOrderID"
    type: str = "STRING"
    value: FIXString
