
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class UnderlyingIssueDate(FIXFieldBase):
    """FIX UnderlyingIssueDate field."""
    tag: str = "242"
    name: str = "UnderlyingIssueDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
