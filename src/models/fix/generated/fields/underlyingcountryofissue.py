
from .base import FIXFieldBase
from .types import FIXCountry

class UnderlyingCountryOfIssue(FIXFieldBase):
    """FIX UnderlyingCountryOfIssue field."""
    tag: str = "592"
    name: str = "UnderlyingCountryOfIssue"
    type: str = "COUNTRY"
    value: FIXCountry
