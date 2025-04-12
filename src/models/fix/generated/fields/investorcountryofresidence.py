
from .base import FIXFieldBase
from .types import FIXCountry

class InvestorCountryOfResidence(FIXFieldBase):
    """FIX InvestorCountryOfResidence field."""
    tag: str = "475"
    name: str = "InvestorCountryOfResidence"
    type: str = "COUNTRY"
    value: FIXCountry
