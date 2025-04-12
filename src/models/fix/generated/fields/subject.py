
from .base import FIXFieldBase
from .types import FIXString

class Subject(FIXFieldBase):
    """FIX Subject field."""
    tag: str = "147"
    name: str = "Subject"
    type: str = "STRING"
    value: FIXString
