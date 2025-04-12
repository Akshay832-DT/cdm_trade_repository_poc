
from .base import FIXFieldBase
from .types import FIXNumInGroup

class NoCollInquiryQualifier(FIXFieldBase):
    """FIX NoCollInquiryQualifier field."""
    tag: str = "938"
    name: str = "NoCollInquiryQualifier"
    type: str = "NUMINGROUP"
    value: FIXNumInGroup
