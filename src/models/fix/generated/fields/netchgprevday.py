
from .base import FIXFieldBase
from .types import FIXString

class NetChgPrevDay(FIXFieldBase):
    """FIX NetChgPrevDay field."""
    tag: str = "451"
    name: str = "NetChgPrevDay"
    type: str = "PRICEOFFSET"
    value: FIXString
