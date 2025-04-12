
from .base import FIXFieldBase
from .types import FIXString

class TestReqID(FIXFieldBase):
    """FIX TestReqID field."""
    tag: str = "112"
    name: str = "TestReqID"
    type: str = "STRING"
    value: FIXString
