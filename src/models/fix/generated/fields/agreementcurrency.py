
from .base import FIXFieldBase
from .types import FIXCurrency

class AgreementCurrency(FIXFieldBase):
    """FIX AgreementCurrency field."""
    tag: str = "918"
    name: str = "AgreementCurrency"
    type: str = "CURRENCY"
    value: FIXCurrency
