
from .base import FIXFieldBase
from .types import FIXInt

class Product(FIXFieldBase):
    """FIX Product field."""
    tag: str = "460"
    name: str = "Product"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: AGENCY
    # 2: COMMODITY
    # 3: CORPORATE
    # 4: CURRENCY
    # 5: EQUITY
    # 6: GOVERNMENT
    # 7: INDEX
    # 8: LOAN
    # 9: MONEYMARKET
    # 10: MORTGAGE
    # 11: MUNICIPAL
    # 12: OTHER
    # 13: FINANCING
