
from .base import FIXFieldBase
from .types import FIXBoolean

class ContraryInstructionIndicator(FIXFieldBase):
    """FIX ContraryInstructionIndicator field."""
    tag: str = "719"
    name: str = "ContraryInstructionIndicator"
    type: str = "BOOLEAN"
    value: FIXBoolean
