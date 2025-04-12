
from .base import FIXFieldBase
from .types import FIXString

class ContraLegRefID(FIXFieldBase):
    """FIX ContraLegRefID field."""
    tag: str = "655"
    name: str = "ContraLegRefID"
    type: str = "STRING"
    value: FIXString
