
from .base import FIXFieldBase
from .types import FIXChar

class AssignmentMethod(FIXFieldBase):
    """FIX AssignmentMethod field."""
    tag: str = "744"
    name: str = "AssignmentMethod"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # R: RANDOM
    # P: PRO_RATA
