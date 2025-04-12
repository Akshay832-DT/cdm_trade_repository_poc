
from .base import FIXFieldBase
from .types import FIXInt

class NoRpts(FIXFieldBase):
    """FIX NoRpts field."""
    tag: str = "82"
    name: str = "NoRpts"
    type: str = "INT"
    value: FIXInt
