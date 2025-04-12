
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class LegIssueDate(FIXFieldBase):
    """FIX LegIssueDate field."""
    tag: str = "249"
    name: str = "LegIssueDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
