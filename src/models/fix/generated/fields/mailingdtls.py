
from .base import FIXFieldBase
from .types import FIXString

class MailingDtls(FIXFieldBase):
    """FIX MailingDtls field."""
    tag: str = "474"
    name: str = "MailingDtls"
    type: str = "STRING"
    value: FIXString
