
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class AgreementDate(FIXFieldBase):
    """FIX AgreementDate field."""
    tag: str = "915"
    name: str = "AgreementDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
