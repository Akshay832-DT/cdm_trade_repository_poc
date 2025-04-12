
from .base import FIXFieldBase
from .types import FIXInt

class SecurityResponseType(FIXFieldBase):
    """FIX SecurityResponseType field."""
    tag: str = "323"
    name: str = "SecurityResponseType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: ACCEPT_AS_IS
    # 2: ACCEPT_WITH_REVISIONS
    # 5: REJECT_SECURITY_PROPOSAL
    # 6: CANNOT_MATCH_SELECTION_CRITERIA
