
from .base import FIXFieldBase
from .types import FIXInt

class MultiLegRptTypeReq(FIXFieldBase):
    """FIX MultiLegRptTypeReq field."""
    tag: str = "563"
    name: str = "MultiLegRptTypeReq"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: REPORT_BY_MULITLEG_SECURITY_ONLY
    # 1: REPORT_BY_MULTILEG_SECURITY_AND_INSTRUMENT_LEGS
    # 2: REPORT_BY_INSTRUMENT_LEGS_ONLY
