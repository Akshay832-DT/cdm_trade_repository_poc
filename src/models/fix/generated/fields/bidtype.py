
from .base import FIXFieldBase
from .types import FIXInt

class BidType(FIXFieldBase):
    """FIX BidType field."""
    tag: str = "394"
    name: str = "BidType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: NON_DISCLOSED
    # 2: DISCLOSED
    # 3: NO_BIDDING_PROCESS
