
from .base import FIXFieldBase
from .types import FIXString

class NewPassword(FIXFieldBase):
    """FIX NewPassword field."""
    tag: str = "925"
    name: str = "NewPassword"
    type: str = "STRING"
    value: FIXString
