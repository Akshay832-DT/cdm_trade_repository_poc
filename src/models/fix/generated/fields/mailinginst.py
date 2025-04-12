
from .base import FIXFieldBase
from .types import FIXString

class MailingInst(FIXFieldBase):
    """FIX MailingInst field."""
    tag: str = "482"
    name: str = "MailingInst"
    type: str = "STRING"
    value: FIXString
