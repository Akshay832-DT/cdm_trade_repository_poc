
from .base import FIXFieldBase
from .types import FIXInt

class BusinessRejectReason(FIXFieldBase):
    """FIX BusinessRejectReason field."""
    tag: str = "380"
    name: str = "BusinessRejectReason"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: OTHER
    # 1: UNKNOWN_ID
    # 2: UNKNOWN_SECURITY
    # 3: UNSUPPORTED_MESSAGE_TYPE
    # 4: APPLICATION_NOT_AVAILABLE
    # 5: CONDITIONALLY_REQUIRED_FIELD_MISSING
    # 6: NOT_AUTHORIZED
    # 7: DELIVER_TO_FIRM_NOT_AVAILABLE_AT_THIS_TIME
