
from .base import FIXFieldBase
from .types import FIXString

class CollAsgnRefID(FIXFieldBase):
    """FIX CollAsgnRefID field."""
    tag: str = "907"
    name: str = "CollAsgnRefID"
    type: str = "STRING"
    value: FIXString
