
from .base import FIXFieldBase
from .types import FIXString

class LegRepoCollateralSecurityType(FIXFieldBase):
    """FIX LegRepoCollateralSecurityType field."""
    tag: str = "250"
    name: str = "LegRepoCollateralSecurityType"
    type: str = "STRING"
    value: FIXString
