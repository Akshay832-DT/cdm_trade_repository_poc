
from .base import FIXFieldBase
from .types import FIXInt

class TaxAdvantageType(FIXFieldBase):
    """FIX TaxAdvantageType field."""
    tag: str = "495"
    name: str = "TaxAdvantageType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: NONE
    # 1: MAXI_ISA
    # 2: TESSA
    # 3: MINI_CASH_ISA
    # 4: MINI_STOCKS_AND_SHARES_ISA
    # 5: MINI_INSURANCE_ISA
    # 6: CURRENT_YEAR_PAYMENT
    # 7: PRIOR_YEAR_PAYMENT
    # 8: ASSET_TRANSFER
    # 9: EMPLOYEE_PRIOR_YEAR
    # 10: EMPLOYEE_CURRENT_YEAR
    # 11: EMPLOYER_PRIOR_YEAR
    # 12: EMPLOYER_CURRENT_YEAR
    # 13: NON_FUND_PROTOTYPE_IRA
    # 14: NON_FUND_QUALIFIED_PLAN
    # 15: DEFINED_CONTRIBUTION_PLAN
    # 16: IRA
    # 17: IRA_ROLLOVER
    # 18: KEOGH
    # 19: PROFIT_SHARING_PLAN
    # 20: US401_K
    # 21: SELF_DIRECTED_IRA
    # 22: US403B
    # 23: US457
    # 24: ROTH_IRA_PROTOTYPE
    # 25: ROTH_IRA_NON_PROTOTYPE
    # 26: ROTH_CONVERSION_IRA_PROTOTYPE
    # 27: ROTH_CONVERSION_IRA_NON_PROTOTYPE
    # 28: EDUCATION_IRA_PROTOTYPE
    # 29: EDUCATION_IRA_NON_PROTOTYPE
