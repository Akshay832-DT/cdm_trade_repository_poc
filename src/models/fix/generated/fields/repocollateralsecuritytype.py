
from .base import FIXFieldBase
from .types import FIXString

class RepoCollateralSecurityType(FIXFieldBase):
    """FIX RepoCollateralSecurityType field."""
    tag: str = "239"
    name: str = "RepoCollateralSecurityType"
    type: str = "STRING"
    value: FIXString
