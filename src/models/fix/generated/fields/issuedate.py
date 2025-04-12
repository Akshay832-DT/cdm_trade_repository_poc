
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class IssueDate(FIXFieldBase):
    """FIX IssueDate field."""
    tag: str = "225"
    name: str = "IssueDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
