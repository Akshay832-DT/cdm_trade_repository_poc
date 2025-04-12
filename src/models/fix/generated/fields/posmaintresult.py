
from .base import FIXFieldBase
from .types import FIXInt

class PosMaintResult(FIXFieldBase):
    """FIX PosMaintResult field."""
    tag: str = "723"
    name: str = "PosMaintResult"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: SUCCESSFUL_COMPLETION
    # 1: REJECTED
    # 99: OTHER
