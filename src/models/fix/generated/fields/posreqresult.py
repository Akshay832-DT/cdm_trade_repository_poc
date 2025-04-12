
from .base import FIXFieldBase
from .types import FIXInt

class PosReqResult(FIXFieldBase):
    """FIX PosReqResult field."""
    tag: str = "728"
    name: str = "PosReqResult"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: VALID_REQUEST
    # 1: INVALID_OR_UNSUPPORTED_REQUEST
    # 2: NO_POSITIONS_FOUND_THAT_MATCH_CRITERIA
    # 3: NOT_AUTHORIZED_TO_REQUEST_POSITIONS
    # 4: REQUEST_FOR_POSITION_NOT_SUPPORTED
    # 99: OTHER
