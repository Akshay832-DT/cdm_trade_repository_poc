
from .base import FIXFieldBase
from .types import FIXString

class SecurityResponseID(FIXFieldBase):
    """FIX SecurityResponseID field."""
    tag: str = "322"
    name: str = "SecurityResponseID"
    type: str = "STRING"
    value: FIXString
