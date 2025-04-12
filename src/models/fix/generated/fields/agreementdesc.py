
from .base import FIXFieldBase
from .types import FIXString

class AgreementDesc(FIXFieldBase):
    """FIX AgreementDesc field."""
    tag: str = "913"
    name: str = "AgreementDesc"
    type: str = "STRING"
    value: FIXString
