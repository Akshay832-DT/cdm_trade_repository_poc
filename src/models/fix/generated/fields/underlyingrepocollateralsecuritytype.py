
from .base import FIXFieldBase
from .types import FIXString

class UnderlyingRepoCollateralSecurityType(FIXFieldBase):
    """FIX UnderlyingRepoCollateralSecurityType field."""
    tag: str = "243"
    name: str = "UnderlyingRepoCollateralSecurityType"
    type: str = "STRING"
    value: FIXString
