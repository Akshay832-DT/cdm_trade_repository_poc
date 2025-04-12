
from .base import FIXFieldBase
from .types import FIXQty

class AssignmentUnit(FIXFieldBase):
    """FIX AssignmentUnit field."""
    tag: str = "745"
    name: str = "AssignmentUnit"
    type: str = "QTY"
    value: FIXQty
