
from .base import FIXFieldBase
from .types import FIXInt

class AcctIDSource(FIXFieldBase):
    """FIX AcctIDSource field."""
    tag: str = "660"
    name: str = "AcctIDSource"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: BIC
    # 2: SID_CODE
    # 3: TFM
    # 4: OMGEO
    # 5: DTCC_CODE
    # 99: OTHER
