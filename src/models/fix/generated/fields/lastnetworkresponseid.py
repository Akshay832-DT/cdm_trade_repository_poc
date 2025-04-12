
from .base import FIXFieldBase
from .types import FIXString

class LastNetworkResponseID(FIXFieldBase):
    """FIX LastNetworkResponseID field."""
    tag: str = "934"
    name: str = "LastNetworkResponseID"
    type: str = "STRING"
    value: FIXString
