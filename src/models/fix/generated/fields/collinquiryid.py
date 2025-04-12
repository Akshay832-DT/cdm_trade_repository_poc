
from .base import FIXFieldBase
from .types import FIXString

class CollInquiryID(FIXFieldBase):
    """FIX CollInquiryID field."""
    tag: str = "909"
    name: str = "CollInquiryID"
    type: str = "STRING"
    value: FIXString
