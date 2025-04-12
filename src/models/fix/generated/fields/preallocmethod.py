
from .base import FIXFieldBase
from .types import FIXChar

class PreallocMethod(FIXFieldBase):
    """FIX PreallocMethod field."""
    tag: str = "591"
    name: str = "PreallocMethod"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 0: PRO_RATA
    # 1: DO_NOT_PRO_RATA
