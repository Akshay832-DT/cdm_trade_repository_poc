
from .base import FIXFieldBase
from .types import FIXInt

class TotNoSecurityTypes(FIXFieldBase):
    """FIX TotNoSecurityTypes field."""
    tag: str = "557"
    name: str = "TotNoSecurityTypes"
    type: str = "INT"
    value: FIXInt
