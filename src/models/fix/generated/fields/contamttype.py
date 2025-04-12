
from .base import FIXFieldBase
from .types import FIXInt

class ContAmtType(FIXFieldBase):
    """FIX ContAmtType field."""
    tag: str = "519"
    name: str = "ContAmtType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: COMMISSION_AMOUNT
    # 2: COMMISSION_PERCENT
    # 3: INITIAL_CHARGE_AMOUNT
    # 4: INITIAL_CHARGE_PERCENT
    # 5: DISCOUNT_AMOUNT
    # 6: DISCOUNT_PERCENT
    # 7: DILUTION_LEVY_AMOUNT
    # 8: DILUTION_LEVY_PERCENT
    # 9: EXIT_CHARGE_AMOUNT
    # 10: EXIT_CHARGE_PERCENT
    # 11: FUND_BASED_RENEWAL_COMMISSION_PERCENT
    # 12: PROJECTED_FUND_VALUE
    # 13: FUND_BASED_RENEWAL_COMMISSION_ON_ORDER
    # 14: FUND_BASED_RENEWAL_COMMISSION_ON_FUND
    # 15: NET_SETTLEMENT_AMOUNT
