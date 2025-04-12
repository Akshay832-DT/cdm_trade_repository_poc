
from .base import FIXFieldBase
from .types import FIXString

class RegistDtls(FIXFieldBase):
    """FIX RegistDtls field."""
    tag: str = "509"
    name: str = "RegistDtls"
    type: str = "STRING"
    value: FIXString
