
from .base import FIXFieldBase
from .types import FIXInt

class ResponseTransportType(FIXFieldBase):
    """FIX ResponseTransportType field."""
    tag: str = "725"
    name: str = "ResponseTransportType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: INBAND
    # 1: OUT_OF_BAND
