
from .base import FIXFieldBase
from .types import FIXInt

class SecurityRequestResult(FIXFieldBase):
    """FIX SecurityRequestResult field."""
    tag: str = "560"
    name: str = "SecurityRequestResult"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: VALID_REQUEST
    # 1: INVALID_OR_UNSUPPORTED_REQUEST
    # 2: NO_INSTRUMENTS_FOUND
    # 3: NOT_AUTHORIZED_TO_RETRIEVE_INSTRUMENT_DATA
    # 4: INSTRUMENT_DATA_TEMPORARILY_UNAVAILABLE
    # 5: REQUEST_FOR_INSTRUMENT_DATA_NOT_SUPPORTED
