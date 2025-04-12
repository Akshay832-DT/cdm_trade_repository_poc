
from .base import FIXFieldBase
from .types import FIXInt

class CPProgram(FIXFieldBase):
    """FIX CPProgram field."""
    tag: str = "875"
    name: str = "CPProgram"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: PROGRAM3A3
    # 2: PROGRAM42
    # 99: OTHER
