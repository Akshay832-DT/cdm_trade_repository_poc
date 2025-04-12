
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class DatedDate(FIXFieldBase):
    """FIX DatedDate field."""
    tag: str = "873"
    name: str = "DatedDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
