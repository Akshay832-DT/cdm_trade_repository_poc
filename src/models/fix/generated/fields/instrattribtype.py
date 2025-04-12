
from .base import FIXFieldBase
from .types import FIXInt

class InstrAttribType(FIXFieldBase):
    """FIX InstrAttribType field."""
    tag: str = "871"
    name: str = "InstrAttribType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: FLAT
    # 2: ZERO_COUPON
    # 3: INTEREST_BEARING
    # 4: NO_PERIODIC_PAYMENTS
    # 5: VARIABLE_RATE
    # 6: LESS_FEE_FOR_PUT
    # 7: STEPPED_COUPON
    # 8: COUPON_PERIOD
    # 9: WHEN
    # 10: ORIGINAL_ISSUE_DISCOUNT
    # 11: CALLABLE
    # 12: ESCROWED_TO_MATURITY
    # 13: ESCROWED_TO_REDEMPTION_DATE
    # 14: PRE_REFUNDED
    # 15: IN_DEFAULT
    # 16: UNRATED
    # 17: TAXABLE
    # 18: INDEXED
    # 19: SUBJECT_TO_ALTERNATIVE_MINIMUM_TAX
    # 20: ORIGINAL_ISSUE_DISCOUNT_PRICE
    # 21: CALLABLE_BELOW_MATURITY_VALUE
    # 22: CALLABLE_WITHOUT_NOTICE
    # 99: TEXT
