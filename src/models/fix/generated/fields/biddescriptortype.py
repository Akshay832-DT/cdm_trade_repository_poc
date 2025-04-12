
from .base import FIXFieldBase
from .types import FIXInt

class BidDescriptorType(FIXFieldBase):
    """FIX BidDescriptorType field."""
    tag: str = "399"
    name: str = "BidDescriptorType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: SECTOR
    # 2: COUNTRY
    # 3: INDEX
