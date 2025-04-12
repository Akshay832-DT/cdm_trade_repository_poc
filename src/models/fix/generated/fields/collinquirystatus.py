
from .base import FIXFieldBase
from .types import FIXInt

class CollInquiryStatus(FIXFieldBase):
    """FIX CollInquiryStatus field."""
    tag: str = "945"
    name: str = "CollInquiryStatus"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: ACCEPTED
    # 1: ACCEPTED_WITH_WARNINGS
    # 2: COMPLETED
    # 3: COMPLETED_WITH_WARNINGS
    # 4: REJECTED
